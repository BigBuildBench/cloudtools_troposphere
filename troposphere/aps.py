# Copyright (c) 2012-2024, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags


class RuleGroupsNamespace(AWSObject):
    """
    `RuleGroupsNamespace <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-rulegroupsnamespace.html>`__
    """

    resource_type = "AWS::APS::RuleGroupsNamespace"

    props: PropsDictType = {
        "Data": (str, True),
        "Name": (str, True),
        "Tags": (Tags, False),
        "Workspace": (str, True),
    }


class AmpConfiguration(AWSProperty):
    """
    `AmpConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-scraper-ampconfiguration.html>`__
    """

    props: PropsDictType = {
        "WorkspaceArn": (str, True),
    }


class Destination(AWSProperty):
    """
    `Destination <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-scraper-destination.html>`__
    """

    props: PropsDictType = {
        "AmpConfiguration": (AmpConfiguration, True),
    }


class ScrapeConfiguration(AWSProperty):
    """
    `ScrapeConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-scraper-scrapeconfiguration.html>`__
    """

    props: PropsDictType = {
        "ConfigurationBlob": (str, True),
    }


class EksConfiguration(AWSProperty):
    """
    `EksConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-scraper-eksconfiguration.html>`__
    """

    props: PropsDictType = {
        "ClusterArn": (str, True),
        "SecurityGroupIds": ([str], False),
        "SubnetIds": ([str], True),
    }


class Source(AWSProperty):
    """
    `Source <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-scraper-source.html>`__
    """

    props: PropsDictType = {
        "EksConfiguration": (EksConfiguration, True),
    }


class Scraper(AWSObject):
    """
    `Scraper <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-scraper.html>`__
    """

    resource_type = "AWS::APS::Scraper"

    props: PropsDictType = {
        "Alias": (str, False),
        "Destination": (Destination, True),
        "ScrapeConfiguration": (ScrapeConfiguration, True),
        "Source": (Source, True),
        "Tags": (Tags, False),
    }


class LoggingConfiguration(AWSProperty):
    """
    `LoggingConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-workspace-loggingconfiguration.html>`__
    """

    props: PropsDictType = {
        "LogGroupArn": (str, False),
    }


class Workspace(AWSObject):
    """
    `Workspace <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-workspace.html>`__
    """

    resource_type = "AWS::APS::Workspace"

    props: PropsDictType = {
        "AlertManagerDefinition": (str, False),
        "Alias": (str, False),
        "KmsKeyArn": (str, False),
        "LoggingConfiguration": (LoggingConfiguration, False),
        "Tags": (Tags, False),
    }