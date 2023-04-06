from django.urls import path

from Backend_Management_App import views, manage_room_bed_views, admin_views, manage_staff_views, manage_student_views, staff_views, student_views
from Backend_Management_App.manage_dept_session_views import *
from Backend_Management_App.admin_views import *





urlpatterns = [

    path('student_feedback_message/', admin_views.studentFeedbackMessage, name="student_feedback_message"),
    path('student_feedback_message_reply/', admin_views.studentFeedbackMessageReply, name="student_feedback_message_reply"),
    
    path('staff_feedback_message/', admin_views.staffFeedbackMessage, name="staff_feedback_message"),
    path('staff_feedback_message_reply/', admin_views.staffFeedbackMessageReply, name="staff_feedback_message_reply"),
    
    # *******************  ROOM MANAGE URL  *****************
    path('manage_room/', manage_room_bed_views.manageRoom, name="manage_room"),
    path('add_room/', manage_room_bed_views.addRoom, name="add_room"),
    path('edit_room/<str:room_number>', manage_room_bed_views.editRoom, name="edit_room"),
    path('delete_room/<str:room_number>', manage_room_bed_views.deleteRoom, name="delete_room"),
    path('add_room_save/', manage_room_bed_views.addRoomSave, name="add_room_save"),
    path('edit_room_save/', manage_room_bed_views.editRoomSave, name="edit_room_save"),

    # *******************  BED MANAGE URL  *****************
    path('manage_bed/', manage_room_bed_views.manageBed, name="manage_bed"),
    path('add_bed/', manage_room_bed_views.addBed, name="add_bed"),
    path('edit_bed/<str:bed_name>', manage_room_bed_views.editBed, name="edit_bed"),
    path('delete_bed/<str:bed_name>', manage_room_bed_views.deleteBed, name="delete_bed"),
    path('add_bed_save/', manage_room_bed_views.addBedSave, name="add_bed_save"),
    path('edit_bed_save/', manage_room_bed_views.editBedSave, name="edit_bed_save"),
    
    # *******************  STAFF MANAGE URL  *****************
    path('manage_staff/', manage_staff_views.manageStaff, name="manage_staff"),
    path('add_staff/', manage_staff_views.addStaff, name="add_staff"),
    path('edit_staff/<str:staff_id>', manage_staff_views.editStaff, name="edit_staff"),
    path('delete_staff/<str:staff_id>', manage_staff_views.deleteStaff, name="delete_staff"),
    path('add_staff_save/', manage_staff_views.addStaffSave, name="add_staff_save"),
    path('edit_staff_save/', manage_staff_views.editStaffSave, name="edit_staff_save"),

    # *******************  StaffView MANAGE URL  *****************
    path('staff_home/', staff_views.staffHome, name="staff_home"),
    path('staff_take_attendence/', staff_views.staffTakeAttendence, name="staff_take_attendence"),
    path('staff_take_attendence/', staff_views.staffTakeAttendence, name="staff_take_attendence"),
    path('get_student/', staff_views.getStudents, name="get_student"),
    path('save_attendence_data/', staff_views.saveAttendenceData, name="save_attendence_data"),
    
    path('staff_update_attendence/', staff_views.staffUpdateAttendence, name="staff_update_attendence"),
    path('get_attendence_date/', staff_views.getAttendenceDates, name="get_attendence_date"),
    path('get_attendence_student/', staff_views.getAttendenceStudents, name="get_attendence_student"),
    path('save_updateattendence_data/', staff_views.saveUpdateAttendenceData, name="save_updateattendence_data"),

    path('staff_feedback/', staff_views.staffFeedback, name="staff_feedback"),
    path('staff_feedback_save/', staff_views.saveStaffFeedback, name="staff_feedback_save"),

     
    # *******************  STUDENT MANAGE URL  *****************
    path('manage_student/', manage_student_views.manageStudent, name="manage_student"),
    path('add_student/', manage_student_views.addStudent, name="add_student"),
    path('edit_student/<str:student_id>', manage_student_views.editStudent, name="edit_student"),
    path('delete_student/<str:student_id>', manage_student_views.deleteStudent, name="delete_student"),
    path('add_student_save/', manage_student_views.addStudentSave, name="add_student_save"),
    path('edit_student_save/', manage_student_views.editStudentSave, name="edit_student_save"),
    
    
    # *******************  StudentView MANAGE URL  *****************
    path('student_home/', student_views.studentHome, name="student_home"),
    path('student_view_attendence/', student_views.studentViewAttendence, name="student_view_attendence"),
    path('student_get_attendence/', student_views.studentGetAttendence, name="student_get_attendence"),
    path('profile_view/', student_views.profile_view, name="profile_view"),

    path('student_feedback/', student_views.studentFeedback, name="student_feedback"),
    path('student_feedback_save/', student_views.saveStudentFeedback, name="student_feedback_save"),
    

    # *******************  Department MANAGE URL  *****************
    path('manage_department/', DepartmentListView.as_view(), name='manage_department'),
    path('add_department/', DepartmentCreateView.as_view(), name='add_department'),
    path('delete_department/<int:pk>/', DepartmentDeleteView.as_view(), name='delete_department'),
    
    # *******************  Session MANAGE URL  *****************
    path('manage_session/', Academic_SessionListView.as_view(), name='manage_session'),
    path('add_session/', Academic_SessionCreateView.as_view(), name='add_session'),
    path('delete_session/<int:pk>/', Academic_SessionDeleteView.as_view(), name='delete_session'),
    
    # *******************  Notice MANAGE URL  *****************
    path('notice_list/', NoticeListView.as_view(), name='notice_list'),
    path('create_notice/', NoticeCreateView.as_view(), name='create_notice'),
    path('update_notice/<int:pk>/', NoticeUpdateView.as_view(), name='update_notice'),
    path('delete_notice/<int:pk>/', NoticeDeleteView.as_view(), name='delete_notice'),



    path('index/', views.BackendController),
    path('login/',views.LoginPage, name="login"),
    path('user_details/',views.GetUserDetails),
    path('logout_user/',views.logout_user, name="logout"),
    path('dologin/',views.doLogin, name="do_login"),
    path('admin_home/', admin_views.admin_home, name="admin_home"),
    path('check_email/', admin_views.checkEmail, name="check_email"),
    path('check_username/', admin_views.checkUsername, name="check_username"),
    path('check_registration/', admin_views.checkRegistration, name="check_registration"),
    path('view_attendence/', admin_views.viewAttendence, name="view_attendence"),
    path('get_attendence/', admin_views.getAttendence, name="get_attendence"),

]




"""from django.urls import path
from Backend_Management_App.manage_room_bed_views import RoomListView, RoomCreateView, RoomUpdateView, RoomDeleteView, BedListView, BedCreateView, BedUpdateView, BedDeleteView
from Backend_Management_App.manage_staff_views import StaffListView, StaffCreateView, StaffUpdateView, StaffDeleteView
from Backend_Management_App.manage_student_views import StudentListView, StudentCreateView, StudentUpdateView, StudentDeleteView


urlpatterns = [
    path('manage_room/', RoomListView.as_view(), name='manage_room'),
    path('add_room/', RoomCreateView.as_view(), name='add_room'),
    path('edit_room/<int:pk>/', RoomUpdateView.as_view(), name='edit_room'),
    path('delete_room/<int:pk>/', RoomDeleteView.as_view(), name='delete_room'),


    path('manage_bed/', BedListView.as_view(), name='manage_bed'),
    path('add_bed/', BedCreateView.as_view(), name='add_bed'),
    path('edit_bed/<int:pk>/', BedUpdateView.as_view(), name='edit_bed'),
    path('delete_bed/<int:pk>/', BedDeleteView.as_view(), name='delete_bed'),


    path('manage_staff/', StaffListView.as_view(), name='manage_staff'),
    path('add_staff/', StaffCreateView.as_view(), name='add_staff'),
    path('edit_staff/<int:pk>/', StaffUpdateView.as_view(), name='edit_staff'),
    path('delete_staff/<int:pk>/', StaffDeleteView.as_view(), name='delete_staff'),


    path('manage_student/', StudentListView.as_view(), name='manage_student'),
    path('add_student/', StudentCreateView.as_view(), name='add_student'),
    path('edit_student/<int:pk>', StudentUpdateView.as_view(), name='edit_student'),
    path('delete_student/<int:pk>', StudentDeleteView.as_view(), name='delete_student'),


    path('manage_student/', manage_student_views.manageStudent, name="manage_student"),
    path('add_student/', manage_student_views.addStudent, name="add_student"),
    path('edit_student/<str:student_id>', manage_student_views.editStudent, name="edit_student"),
    path('delete_student/<str:student_id>', manage_student_views.deleteStudent, name="delete_student"),
    path('add_student_save/', manage_student_views.addStudentSave, name="add_student_save"),
    path('edit_student_save/', manage_student_views.editStudentSave, name="edit_student_save"),

]
"""