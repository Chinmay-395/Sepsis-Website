from rest_framework import permissions

""" For doctors to view their own data """


class DoctorProfileView(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        print("REQUEST>>>>>>", request.method)
        print("permissions.SAFE_METHODS>>>>>", permissions.SAFE_METHODS)
        print(">>>>>>>>>> ", request.user)
        # ID in the user-Profile
        print(">>>>>>>>>>REQUEST-ID ", request.user.id)
        # ID in the Doctor model
        print(">>>>>>>>>>OBJECT-ID ", obj.id)
        print(">>>>>>>>>>REQUEST-username ", request.user)
        print(">>>>>>>>>>OBJECT-username ", obj)
        print(">>>>>>>>>>OBJECT-email ", obj.doc.email)
        if request.method in permissions.SAFE_METHODS:
            print(">>>>>>>>>> ", type(request.user.name))
            requesting_user = request.user.name
            print(">>>>>>>>>> ", type(obj))
            obj_user = obj.doc.name
            """ I will be using username to match the doctor with requested_user
                Key-Point: make sure <obj_user> & <requesting_user> are
                           are "email" fields since email of each UserProfile model
                           is unique
            """
            if(obj_user == requesting_user):
                return True
            else:
                return False
            # return True

        # if request.method in
        return obj.id == request.user.id


""" For Patients to view their own data """


class PatientProfileView(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        print("REQUEST>>>>>>", request.method)
        print("permissions.SAFE_METHODS>>>>>", permissions.SAFE_METHODS)
        if request.method in permissions.SAFE_METHODS:
            print(">>>>>>>>>> ", request.user)
            print(">>>>>>>>>> ", obj)
            print("__________", request.user.id)
            print("OBJECT-ID>>>>>>>>>", obj.id)
            print("OBJECT_PAT_ID", obj.pat.id)
            print("OBJ-EMAIL", obj.pat.email)
            print("REQUEST-EMAIL", request.user.email)
            if(request.user.id == obj.pat.id):
                return True
            else:
                return False

        # if request.method in
        return obj.id == request.user.id
