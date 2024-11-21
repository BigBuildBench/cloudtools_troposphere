# Copyright (c) 2012-2024, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import double


class AWSAccount(AWSProperty):
    """
    `AWSAccount <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-awsaccount.html>`__
    """

    props: PropsDictType = {
        "EmailAddress": (str, False),
        "Id": (str, False),
        "Name": (str, False),
    }


class AssessmentReportsDestination(AWSProperty):
    """
    `AssessmentReportsDestination <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-assessmentreportsdestination.html>`__
    """

    props: PropsDictType = {
        "Destination": (str, False),
        "DestinationType": (str, False),
    }


class Delegation(AWSProperty):
    """
    `Delegation <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-delegation.html>`__
    """

    props: PropsDictType = {
        "AssessmentId": (str, False),
        "AssessmentName": (str, False),
        "Comment": (str, False),
        "ControlSetId": (str, False),
        "CreatedBy": (str, False),
        "CreationTime": (double, False),
        "Id": (str, False),
        "LastUpdated": (double, False),
        "RoleArn": (str, False),
        "RoleType": (str, False),
        "Status": (str, False),
    }


class Role(AWSProperty):
    """
    `Role <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-role.html>`__
    """

    props: PropsDictType = {
        "RoleArn": (str, False),
        "RoleType": (str, False),
    }


class AWSService(AWSProperty):
    """
    `AWSService <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-awsservice.html>`__
    """

    props: PropsDictType = {
        "ServiceName": (str, False),
    }


class Scope(AWSProperty):
    """
    `Scope <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-scope.html>`__
    """

    props: PropsDictType = {
        "AwsAccounts": ([AWSAccount], False),
        "AwsServices": ([AWSService], False),
    }


class Assessment(AWSObject):
    """
    `Assessment <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-auditmanager-assessment.html>`__
    """

    resource_type = "AWS::AuditManager::Assessment"

    props: PropsDictType = {
        "AssessmentReportsDestination": (AssessmentReportsDestination, False),
        "AwsAccount": (AWSAccount, False),
        "Delegations": ([Delegation], False),
        "Description": (str, False),
        "FrameworkId": (str, False),
        "Name": (str, False),
        "Roles": ([Role], False),
        "Scope": (Scope, False),
        "Status": (str, False),
        "Tags": (Tags, False),
    }