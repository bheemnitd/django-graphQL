# django-graphQL

## Using the tech stack above (This is a must), build a simple blog API service. It should expose a GraphQL endpoint to do the folloing things:

#### Implement a createPost() mutation which will create a Post (a blogpost object) with attributes {title, description, publish_date, author (just a name as TextField)}

### Implement a updatePost($id) mutation which will update a Post attributes by $id

### Implement a createComment() mutation which will create a Comment object with attributes {post (the blogpost object), text, author (just the name as a TextField)}

### Implement a deleteComment($id) mutation to delete the given Comment by its ID.

### Implement a posts() query to list all the posts

### Implement a post($id) query to get details of a post and all its comments12
