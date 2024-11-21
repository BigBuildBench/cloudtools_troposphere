# Copyright (c) 2012-2024, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType
from .validators import boolean, integer


class ModuleLoggingConfiguration(AWSProperty):
    """
    `ModuleLoggingConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-moduleloggingconfiguration.html>`__
    """

    props: PropsDictType = {
        "CloudWatchLogGroupArn": (str, False),
        "Enabled": (boolean, False),
        "LogLevel": (str, False),
    }


class LoggingConfiguration(AWSProperty):
    """
    `LoggingConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-loggingconfiguration.html>`__
    """

    props: PropsDictType = {
        "DagProcessingLogs": (ModuleLoggingConfiguration, False),
        "SchedulerLogs": (ModuleLoggingConfiguration, False),
        "TaskLogs": (ModuleLoggingConfiguration, False),
        "WebserverLogs": (ModuleLoggingConfiguration, False),
        "WorkerLogs": (ModuleLoggingConfiguration, False),
    }


class NetworkConfiguration(AWSProperty):
    """
    `NetworkConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-networkconfiguration.html>`__
    """

    props: PropsDictType = {
        "SecurityGroupIds": ([str], False),
        "SubnetIds": ([str], False),
    }


class Environment(AWSObject):
    """
    `Environment <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html>`__
    """

    resource_type = "AWS::MWAA::Environment"

    props: PropsDictType = {
        "AirflowConfigurationOptions": (dict, False),
        "AirflowVersion": (str, False),
        "DagS3Path": (str, False),
        "EndpointManagement": (str, False),
        "EnvironmentClass": (str, False),
        "ExecutionRoleArn": (str, False),
        "KmsKey": (str, False),
        "LoggingConfiguration": (LoggingConfiguration, False),
        "MaxWebservers": (integer, False),
        "MaxWorkers": (integer, False),
        "MinWebservers": (integer, False),
        "MinWorkers": (integer, False),
        "Name": (str, True),
        "NetworkConfiguration": (NetworkConfiguration, False),
        "PluginsS3ObjectVersion": (str, False),
        "PluginsS3Path": (str, False),
        "RequirementsS3ObjectVersion": (str, False),
        "RequirementsS3Path": (str, False),
        "Schedulers": (integer, False),
        "SourceBucketArn": (str, False),
        "StartupScriptS3ObjectVersion": (str, False),
        "StartupScriptS3Path": (str, False),
        "Tags": (dict, False),
        "WebserverAccessMode": (str, False),
        "WeeklyMaintenanceWindowStart": (str, False),
    }