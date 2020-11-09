from graphene import InputObjectType, String, List, Field, ObjectType, Mutation, Int,Boolean
from graphene_django import DjangoObjectType
from .models import Post, Comment
from graphql import GraphQLError

class PostType(DjangoObjectType):
    class Meta:
        model = Post

class PostInputType(InputObjectType):
    title = String()
    description = String()
    author = String()

class CreatePost(Mutation):
    class Arguments:
        input=PostInputType()
    
    post = Field(PostType)

    def mutate(root, info, input=None):
        post = Post.objects.create(
            title=input.title,
            description=input.description,
            # publish_date=publish_date,
            author=input.author
        )
        return CreatePost(post=post)

class UpdatePost(Mutation):
    class Arguments:
        input=PostInputType()
        id = Int(required=True)

    post=Field(PostType)

    def mutate(root, info, id, input=None):

        try:
            post=Post.objects.get(id=id)

            if input.title:
                post.title=input.title

            if input.description:
                post.description=input.description

            if input.author:
                post.author=input.author

            post.save()    
            
        except Exception:
            raise GraphQLError("id not found!")
        return UpdatePost(post=post)

class CommentType(DjangoObjectType):
    class Meta:
        model = Comment

class CommentInputType(InputObjectType):
    post_id = Int(required=True)
    text = String(required=True)
    author = String()

class CreateComment(Mutation):
    class Arguments:
        input=CommentInputType()

    comment = Field(CommentType)

    def mutate(root, info, input=None):
        comment = Comment.objects.create(
            post_id=input.post_id,
            text=input.text,
            author=input.author
        )
        return CreateComment(comment=comment)
        
class DeleteComment(Mutation):
    success=Boolean()
    class Arguments:
         id=Int()

    def mutate(root, info, id):
        try:
            Comment.objects.get(id=id).delete()
        except Exception:
            raise GraphQLError("Post Id is not available or No comments found for this id !")
        return DeleteComment(success=True)

class Query(ObjectType):

    posts = List(PostType)
    post = Field(PostType, id=Int())
    comments=List(CommentType)
    def resolve_posts(root, info):
        return Post.objects.all()

    def resolve_post(root, info, id):
        try:
            return Post.objects.get(id=id)
        except Exception as e:
            raise GraphQLError(e)

    def resolve_comments(root, info):
        return Comment.objects.all()

class Mutation(ObjectType):
    create_post = CreatePost.Field()
    update_post = UpdatePost.Field()
    create_comment = CreateComment.Field()
    delete_comment = DeleteComment.Field()