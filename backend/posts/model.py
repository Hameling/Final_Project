# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Assign(models.Model):
    memberid = models.ForeignKey('Member', models.DO_NOTHING, db_column='memberid', primary_key=True)
    contentid = models.IntegerField()
    assignid = models.AutoField(unique=True)

    class Meta:
        managed = False
        db_table = 'Assign'
        unique_together = (('memberid', 'contentid'),)


class Calender(models.Model):
    indexnumber = models.AutoField(primary_key=True)
    starttime = models.DateTimeField()
    duetime = models.DateTimeField()
    contentid = models.ForeignKey('Content', models.DO_NOTHING, db_column='contentid')
    isoverlap = models.IntegerField(blank=True, null=True)
    calendername = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'Calender'


class Checklist(models.Model):
    listnumber = models.AutoField(primary_key=True)
    listname = models.CharField(max_length=200, blank=True, null=True)
    contentid = models.ForeignKey('Content', models.DO_NOTHING, db_column='contentid')
    checked = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Checklist'


class Comment(models.Model):
    comnumber = models.AutoField(primary_key=True)
    comcomment = models.CharField(max_length=400, blank=True, null=True)
    contentid = models.ForeignKey('Content', models.DO_NOTHING, db_column='contentid')
    memberid = models.ForeignKey('Member', models.DO_NOTHING, db_column='memberid', blank=True, null=True)
    commenttime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Comment'


class Content(models.Model):
    contentid = models.AutoField(primary_key=True)
    contentname = models.CharField(max_length=200, blank=True, null=True)
    contentinfo = models.CharField(max_length=400, blank=True, null=True)
    contentstate = models.ForeignKey('Contentstate', models.DO_NOTHING, db_column='contentstate')
    sectionid = models.ForeignKey('Section', models.DO_NOTHING, db_column='sectionid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Content'


class Contentstate(models.Model):
    statenumber = models.IntegerField(primary_key=True)
    statename = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'Contentstate'


class Enroll(models.Model):
    memberid = models.ForeignKey('Member', models.DO_NOTHING, db_column='memberid', primary_key=True)
    titleid = models.ForeignKey('Title', models.DO_NOTHING, db_column='titleid')
    enrollid = models.AutoField(unique=True)

    class Meta:
        managed = False
        db_table = 'Enroll'
        unique_together = (('memberid', 'titleid'),)


class File(models.Model):
    contentid = models.ForeignKey(Content, models.DO_NOTHING, db_column='contentid')
    fileid = models.AutoField(primary_key=True)
    filename = models.TextField(blank=True, null=True)
    filerealname = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'File'


class Member(models.Model):
    memberid = models.CharField(primary_key=True, max_length=45)
    membername = models.CharField(max_length=45)
    memberpwd = models.CharField(max_length=45)
    memberemail = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'Member'


class Permission(models.Model):
    priority = models.ForeignKey('Permissionstate', models.DO_NOTHING, db_column='priority')
    memberid = models.ForeignKey(Member, models.DO_NOTHING, db_column='memberid')
    permissionid = models.AutoField(primary_key=True)
    fileid = models.ForeignKey(File, models.DO_NOTHING, db_column='fileid')
    contentid = models.ForeignKey(Content, models.DO_NOTHING, db_column='contentid')

    class Meta:
        managed = False
        db_table = 'Permission'


class Permissionstate(models.Model):
    perstatenumber = models.IntegerField(primary_key=True)
    perstatename = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'Permissionstate'


class Section(models.Model):
    sectionid = models.AutoField(primary_key=True)
    titleid = models.ForeignKey('Title', models.DO_NOTHING, db_column='titleid')
    sectionname = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Section'


class Session(models.Model):
    memberid = models.ForeignKey(Member, models.DO_NOTHING, db_column='memberid')
    token = models.CharField(max_length=120)
    expiretime = models.DateTimeField()
    sessionid = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'Session'


class Title(models.Model):
    titleid = models.AutoField(primary_key=True)
    titlename = models.CharField(max_length=200, blank=True, null=True)
    titleinfo = models.CharField(max_length=400, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Title'


class Uploadfilemodel(models.Model):
    fileid = models.AutoField(primary_key=True)
    filename = models.CharField(max_length=32)
    fileex = models.TextField()

    class Meta:
        managed = False
        db_table = 'UploadFileModel'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Download(models.Model):
    token = models.CharField(primary_key=True, max_length=120)
    contentid = models.IntegerField()
    filename = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'download'
