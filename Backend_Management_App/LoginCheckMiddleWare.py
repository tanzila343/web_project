from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin


class loginCheckMiddleware(MiddlewareMixin):  
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        moduleName = view_func.__module__
        user = request.user

        if request.path == reverse('home') or request.path == reverse('about') or request.path == reverse('contact') or request.path == reverse('service') or request.path == reverse('student_registration')  or request.path == reverse('login') or request.path == reverse('new_student_save') :
            return None

        if user.is_authenticated:
            if request.path == reverse('logout') :
                return None
            
            if user.user_type == "1":
                if moduleName == "Backend_Management_App.admin_views":
                    pass
                elif moduleName == "Backend_Management_App.manage_dept_session_views":
                    pass
                elif moduleName == "Backend_Management_App.manage_room_bed_views":
                    pass
                elif moduleName == "Backend_Management_App.manage_staff_views":
                    pass
                elif moduleName == "Backend_Management_App.manage_student_views":
                    pass
                elif moduleName == "Frontend_Management_App.views":
                    pass
                elif moduleName == "django.views.static":
                    pass
                elif moduleName == "Backend_Management_App.views":
                    pass
                else:
                    return HttpResponseRedirect(reverse("admin_home"))
                
            elif user.user_type == "2":
                if moduleName == "Backend_Management_App.staff_views":
                    pass
                elif moduleName == "Frontend_Management_App.views":
                    pass
                elif moduleName == "Backend_Management_App.views" or moduleName == "django.views.static":
                    pass
                else:
                    return HttpResponseRedirect(reverse("staff_home"))  

            else:
                if moduleName == "Backend_Management_App.student_views":
                    pass
                elif moduleName == "Frontend_Management_App.views":
                    pass
                elif moduleName == "Backend_Management_App.views" or moduleName == "django.views.static":
                    pass
                else:
                    return HttpResponseRedirect(reverse("student_home")) 
            
        else:
            if request.path == reverse("login") or request.path == reverse("do_login") or moduleName == "django.contrib.auth.views" or moduleName == "django.views.static":
                pass
            elif moduleName == "Frontend_Management_App.views":
                    pass
            else:
                return HttpResponseRedirect(reverse("login"))
