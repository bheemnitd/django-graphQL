# django-graphQL


mutation createPost {
createPost(input: {title: "The china Study.",
description: "The China Study is a helth related book.",
author: "Jonathan hui."}) {
post {
id
title
description
publishDate
author
}
}
}

query posts {
posts {
id
title
description
publishDate
author
}
}
query post {
post(id:1) {
id
title
description
publishDate
author
commentSet {
id
text
author
}
}
}
mutation updatePost {
updatePost(id:2, input: {title: "College",
description: "Nalanda University is biggetst University in the world.",
author: "Bheem"}) {
post {
id
title
description
publishDate
author
}
}
}
mutation createComment {
createComment(input: {postId: 1, text: "awesome pic!", author: "sameer"}) {
comment {
id
post {id}
text
author
}
}
}
