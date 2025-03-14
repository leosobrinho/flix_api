from rest_framework import permissions


class GenrePermissionClass(permissions.BasePermission):

    def has_permission(self, request, view):
        # logica da permissao
        if request.method in ['GET', 'OPTIONS', 'HEAD']:  # metodos de leitura
            return request.user.has_perm('genres.view_genre')

        if request.method == 'POST':   # metodo de criacao
            return request.user.has_perm('genres.add_genre')

        if request.method in ['PATCH', 'PUT']:  # metodo de update
            return request.user.has_perm('genres.change_genre')

        if request.method == 'DELETE':
            return request.user.has_perm('genres.delete_genre')

        return False
