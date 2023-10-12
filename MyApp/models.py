from django.db import models
from datetime import date, datetime
from django.contrib.auth.models import User 
from django.urls import reverse







# Create your models here.
class Application(models.Model):
    ApplicationId = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE)
    EventName = models.CharField(max_length=255)
    StartDate = models.DateTimeField(max_length=255)
    EndDate = models.DateTimeField(max_length=255)
    HostCity = models.CharField(max_length=255)
    HostProvince =models.CharField(max_length=255)
    ReportSubmitAgreement = models.BooleanField(default=False)
    NumberOfTeam = models.IntegerField(max_length=255)
    MethodOfSelection = models.CharField(max_length=255)
    SelectionApprovedDate = models.DateField(max_length=255)
    TravelDateTime = models.DateTimeField(max_length=255)
    ModeOfTravel = models.CharField(max_length=255)
    CodeOfConductAcceped = models.BooleanField(default=False)
    RegulationsInterestDeclaration  = models.CharField(max_length=300, default='NotProvided')
    RegulationsInterestDeclaration  = models.CharField(max_length=300, default='NotProvided')
    SelectionCriteriaProtocols = models.CharField(max_length=300, default='NotProvided')
    GeneralRegulationSelectionProcedure  =models.CharField(max_length=300, default='NotProvided')
    DocumentationOfSelectionSubmitted = models.CharField(max_length=300, default='NotProvided')
    TeamOfficialDuties = models.CharField(max_length=300, default='NotProvided') 
    AcceptanceOfTeamAppointment = models.CharField(max_length=300, default='NotProvided')
    HighPerformancePlan = models.CharField(max_length=300, default='NotProvided')
    EventInvitation  = models.CharField(max_length=300, default='NotProvided')
    ApplicationDate  = models.DateTimeField(default=datetime.now())
    Step = models.CharField(max_length=255, default='start')
    ApplicationStatus = models.CharField(max_length=255, default='Oncreate')
    
    

class Represantative(models.Model):
    RepresantativeId = models.AutoField(primary_key=True)
    application = models.ForeignKey(Application,blank=True,null=True,on_delete=models.CASCADE)
    FirstName = models.CharField(max_length=255)
    Surname =models.CharField(max_length=255)
    Gender = models.CharField(max_length=255)
    Event = models.CharField(max_length=255)
    PhoneNumber = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)
    City = models.CharField(max_length=255)
    Province = models.CharField(max_length=255)
    Date = models.DateTimeField(auto_now=False, auto_now_add=True)
    RepresanativeLeve = models.CharField(max_length=255)
    Duration = models.CharField(max_length=255)
    IDCopySubmited = models.BooleanField(default=False,blank=False,null=False)
    AcceptanceofTeamAppointment = models.BooleanField(default=False,blank=False,null=False)
    RepresatativeType = models.CharField(max_length=255, default='Junior')
    

class CommitteeMember(models.Model):
    
    CommitteeMemberId = models.AutoField(primary_key=True)
    application = models.ForeignKey(Application,blank=True,null=True,on_delete=models.CASCADE)
    FirstName = models.CharField(max_length=255)
    Surname = models.CharField(max_length=255)
    Gender = models.CharField(max_length=255)
    Email = models.CharField(max_length=255, default="email")
    PhoneNumber = models.CharField(max_length=255, default="number")
    City = models.CharField(max_length=255, default="city")
    Province = models.CharField(max_length=255, default="province")
    
class TeamOfficial(models.Model):
    TeamOfficialId = models.AutoField(primary_key=True, auto_created=True, null=False, blank=False)
    application = models.ForeignKey(Application,blank=True,null=True,on_delete=models.CASCADE)
    FirstName = models.CharField(max_length=100, blank=False,null=False)
    LastName = models.CharField(max_length=100, blank=False,null=False)
    Gender = models.CharField(max_length=30, null=False, blank=False)
    Designation = models.CharField(max_length=100, blank=False,null=False)
    IDCopySubmited = models.BooleanField(default=False) 
    AcceptanceofTeamAppointment  = models.BooleanField(null=False, blank=False, default=False)

class Thefunctions():
    
    def getObjectCount(list): 
        numObj = 0
        for obj in list:
            numObj += 1
              
        return numObj 
    
    
    


STATUS={
    ('Pending','Pending'),
    ('Approved','Approved'),
    ('Rejected','Rejected'),
}





    
    
    


    
    

   