# Copyright (c) 2012-2024, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags


class Parameter(AWSProperty):
    """
    `Parameter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-controltower-enabledbaseline-parameter.html>`__
    """

    props: PropsDictType = {
        "Key": (str, False),
        "Value": (dict, False),
    }


class EnabledBaseline(AWSObject):
    """
    `EnabledBaseline <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-controltower-enabledbaseline.html>`__
    """

    resource_type = "AWS::ControlTower::EnabledBaseline"

    props: PropsDictType = {
        "BaselineIdentifier": (str, True),
        "BaselineVersion": (str, True),
        "Parameters": ([Parameter], False),
        "Tags": (Tags, False),
        "TargetIdentifier": (str, True),
    }


class EnabledControlParameter(AWSProperty):
    """
    `EnabledControlParameter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-controltower-enabledcontrol-enabledcontrolparameter.html>`__
    """

    props: PropsDictType = {
        "Key": (str, True),
        "Value": (dict, True),
    }


class EnabledControl(AWSObject):
    """
    `EnabledControl <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-controltower-enabledcontrol.html>`__
    """

    resource_type = "AWS::ControlTower::EnabledControl"

    props: PropsDictType = {
        "ControlIdentifier": (str, True),
        "Parameters": ([EnabledControlParameter], False),
        "Tags": (Tags, False),
        "TargetIdentifier": (str, True),
    }


class LandingZone(AWSObject):
    """
    `LandingZone <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-controltower-landingzone.html>`__
    """

    resource_type = "AWS::ControlTower::LandingZone"

    props: PropsDictType = {
        "Manifest": (dict, True),
        "Tags": (Tags, False),
        "Version": (str, True),
    }
