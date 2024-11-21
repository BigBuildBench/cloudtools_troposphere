# Copyright (c) 2012-2024, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean
from .validators.efs import Bursting  # noqa: F401
from .validators.efs import Elastic  # noqa: F401
from .validators.efs import Provisioned  # noqa: F401
from .validators.efs import (
    provisioned_throughput_validator,
    throughput_mode_validator,
    validate_backup_policy,
)


class PosixUser(AWSProperty):
    """
    `PosixUser <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-accesspoint-posixuser.html>`__
    """

    props: PropsDictType = {
        "Gid": (str, True),
        "SecondaryGids": ([str], False),
        "Uid": (str, True),
    }


class CreationInfo(AWSProperty):
    """
    `CreationInfo <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-accesspoint-creationinfo.html>`__
    """

    props: PropsDictType = {
        "OwnerGid": (str, True),
        "OwnerUid": (str, True),
        "Permissions": (str, True),
    }


class RootDirectory(AWSProperty):
    """
    `RootDirectory <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-accesspoint-rootdirectory.html>`__
    """

    props: PropsDictType = {
        "CreationInfo": (CreationInfo, False),
        "Path": (str, False),
    }


class AccessPoint(AWSObject):
    """
    `AccessPoint <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-accesspoint.html>`__
    """

    resource_type = "AWS::EFS::AccessPoint"

    props: PropsDictType = {
        "AccessPointTags": (Tags, False),
        "ClientToken": (str, False),
        "FileSystemId": (str, True),
        "PosixUser": (PosixUser, False),
        "RootDirectory": (RootDirectory, False),
    }


class BackupPolicy(AWSProperty):
    """
    `BackupPolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-filesystem-backuppolicy.html>`__
    """

    props: PropsDictType = {
        "Status": (str, True),
    }

    def validate(self):
        validate_backup_policy(self)


class FileSystemProtection(AWSProperty):
    """
    `FileSystemProtection <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-filesystem-filesystemprotection.html>`__
    """

    props: PropsDictType = {
        "ReplicationOverwriteProtection": (str, False),
    }


class LifecyclePolicy(AWSProperty):
    """
    `LifecyclePolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-filesystem-lifecyclepolicy.html>`__
    """

    props: PropsDictType = {
        "TransitionToArchive": (str, False),
        "TransitionToIA": (str, False),
        "TransitionToPrimaryStorageClass": (str, False),
    }


class ReplicationDestination(AWSProperty):
    """
    `ReplicationDestination <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-filesystem-replicationdestination.html>`__
    """

    props: PropsDictType = {
        "AvailabilityZoneName": (str, False),
        "FileSystemId": (str, False),
        "KmsKeyId": (str, False),
        "Region": (str, False),
    }


class ReplicationConfiguration(AWSProperty):
    """
    `ReplicationConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-filesystem-replicationconfiguration.html>`__
    """

    props: PropsDictType = {
        "Destinations": ([ReplicationDestination], False),
    }


class FileSystem(AWSObject):
    """
    `FileSystem <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-filesystem.html>`__
    """

    resource_type = "AWS::EFS::FileSystem"

    props: PropsDictType = {
        "AvailabilityZoneName": (str, False),
        "BackupPolicy": (BackupPolicy, False),
        "BypassPolicyLockoutSafetyCheck": (boolean, False),
        "Encrypted": (boolean, False),
        "FileSystemPolicy": (dict, False),
        "FileSystemProtection": (FileSystemProtection, False),
        "FileSystemTags": (Tags, False),
        "KmsKeyId": (str, False),
        "LifecyclePolicies": ([LifecyclePolicy], False),
        "PerformanceMode": (str, False),
        "ProvisionedThroughputInMibps": (provisioned_throughput_validator, False),
        "ReplicationConfiguration": (ReplicationConfiguration, False),
        "ThroughputMode": (throughput_mode_validator, False),
    }


class MountTarget(AWSObject):
    """
    `MountTarget <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-mounttarget.html>`__
    """

    resource_type = "AWS::EFS::MountTarget"

    props: PropsDictType = {
        "FileSystemId": (str, True),
        "IpAddress": (str, False),
        "SecurityGroups": ([str], True),
        "SubnetId": (str, True),
    }