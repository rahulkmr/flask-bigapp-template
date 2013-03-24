import views

routes = [
    ('/', 'index', views.post_index),
    ('/<int:id>', 'show', views.post_show),
    ('/new', 'new', views.post_new, {'methods': ['GET', 'POST']}),
    ('/<int:id>/edit', 'edit', views.post_edit, {'methods': ['GET', 'POST']}),
    ('/<int:id>/delete', 'delete', views.post_delete, {'methods': ['POST', 'DELETE']}),

    ('/<int:post_id>/comment_new', 'comment_new', views.comment_new, {'methods': ['GET', 'POST']}),
    ('/<int:post_id>/comment_delete/<int:id>', 'comment_delete', views.comment_delete, {'methods': ['GET', 'POST']}),
]
