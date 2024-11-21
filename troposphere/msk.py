# Copyright (c) 2012-2024, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, integer


class BatchScramSecret(AWSObject):
    """
    `BatchScramSecret <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-batchscramsecret.html>`__
    """

    resource_type = "AWS::MSK::BatchScramSecret"

    props: PropsDictType = {
        "ClusterArn": (str, True),
        "SecretArnList": ([str], False),
    }


class PublicAccess(AWSProperty):
    """
    `PublicAccess <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-publicaccess.html>`__
    """

    props: PropsDictType = {
        "Type": (str, False),
    }


class VpcConnectivityIam(AWSProperty):
    """
    `VpcConnectivityIam <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-vpcconnectivityiam.html>`__
    """

    props: PropsDictType = {
        "Enabled": (boolean, True),
    }


class VpcConnectivityScram(AWSProperty):
    """
    `VpcConnectivityScram <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-vpcconnectivityscram.html>`__
    """

    props: PropsDictType = {
        "Enabled": (boolean, True),
    }


class VpcConnectivitySasl(AWSProperty):
    """
    `VpcConnectivitySasl <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-vpcconnectivitysasl.html>`__
    """

    props: PropsDictType = {
        "Iam": (VpcConnectivityIam, False),
        "Scram": (VpcConnectivityScram, False),
    }


class VpcConnectivityTls(AWSProperty):
    """
    `VpcConnectivityTls <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-vpcconnectivitytls.html>`__
    """

    props: PropsDictType = {
        "Enabled": (boolean, True),
    }


class VpcConnectivityClientAuthentication(AWSProperty):
    """
    `VpcConnectivityClientAuthentication <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-vpcconnectivityclientauthentication.html>`__
    """

    props: PropsDictType = {
        "Sasl": (VpcConnectivitySasl, False),
        "Tls": (VpcConnectivityTls, False),
    }


class VpcConnectivity(AWSProperty):
    """
    `VpcConnectivity <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-vpcconnectivity.html>`__
    """

    props: PropsDictType = {
        "ClientAuthentication": (VpcConnectivityClientAuthentication, False),
    }


class ConnectivityInfo(AWSProperty):
    """
    `ConnectivityInfo <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-connectivityinfo.html>`__
    """

    props: PropsDictType = {
        "PublicAccess": (PublicAccess, False),
        "VpcConnectivity": (VpcConnectivity, False),
    }


class ProvisionedThroughput(AWSProperty):
    """
    `ProvisionedThroughput <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-provisionedthroughput.html>`__
    """

    props: PropsDictType = {
        "Enabled": (boolean, False),
        "VolumeThroughput": (integer, False),
    }


class EBSStorageInfo(AWSProperty):
    """
    `EBSStorageInfo <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-ebsstorageinfo.html>`__
    """

    props: PropsDictType = {
        "ProvisionedThroughput": (ProvisionedThroughput, False),
        "VolumeSize": (integer, False),
    }


class StorageInfo(AWSProperty):
    """
    `StorageInfo <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-storageinfo.html>`__
    """

    props: PropsDictType = {
        "EBSStorageInfo": (EBSStorageInfo, False),
    }


class BrokerNodeGroupInfo(AWSProperty):
    """
    `BrokerNodeGroupInfo <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokernodegroupinfo.html>`__
    """

    props: PropsDictType = {
        "BrokerAZDistribution": (str, False),
        "ClientSubnets": ([str], True),
        "ConnectivityInfo": (ConnectivityInfo, False),
        "InstanceType": (str, True),
        "SecurityGroups": ([str], False),
        "StorageInfo": (StorageInfo, False),
    }


class Iam(AWSProperty):
    """
    `Iam <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-serverlesscluster-iam.html>`__
    """

    props: PropsDictType = {
        "Enabled": (boolean, True),
    }


class Scram(AWSProperty):
    """
    `Scram <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-scram.html>`__
    """

    props: PropsDictType = {
        "Enabled": (boolean, True),
    }


class Sasl(AWSProperty):
    """
    `Sasl <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-sasl.html>`__
    """

    props: PropsDictType = {
        "Iam": (Iam, False),
        "Scram": (Scram, False),
    }


class Tls(AWSProperty):
    """
    `Tls <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-tls.html>`__
    """

    props: PropsDictType = {
        "CertificateAuthorityArnList": ([str], False),
        "Enabled": (boolean, False),
    }


class Unauthenticated(AWSProperty):
    """
    `Unauthenticated <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-unauthenticated.html>`__
    """

    props: PropsDictType = {
        "Enabled": (boolean, True),
    }


class ClientAuthentication(AWSProperty):
    """
    `ClientAuthentication <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-clientauthentication.html>`__
    """

    props: PropsDictType = {
        "Sasl": (Sasl, False),
        "Tls": (Tls, False),
        "Unauthenticated": (Unauthenticated, False),
    }


class ConfigurationInfo(AWSProperty):
    """
    `ConfigurationInfo <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-configurationinfo.html>`__
    """

    props: PropsDictType = {
        "Arn": (str, True),
        "Revision": (integer, True),
    }


class EncryptionAtRest(AWSProperty):
    """
    `EncryptionAtRest <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-encryptionatrest.html>`__
    """

    props: PropsDictType = {
        "DataVolumeKMSKeyId": (str, True),
    }


class EncryptionInTransit(AWSProperty):
    """
    `EncryptionInTransit <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-encryptionintransit.html>`__
    """

    props: PropsDictType = {
        "ClientBroker": (str, False),
        "InCluster": (boolean, False),
    }


class EncryptionInfo(AWSProperty):
    """
    `EncryptionInfo <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-encryptioninfo.html>`__
    """

    props: PropsDictType = {
        "EncryptionAtRest": (EncryptionAtRest, False),
        "EncryptionInTransit": (EncryptionInTransit, False),
    }


class CloudWatchLogs(AWSProperty):
    """
    `CloudWatchLogs <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-cloudwatchlogs.html>`__
    """

    props: PropsDictType = {
        "Enabled": (boolean, True),
        "LogGroup": (str, False),
    }


class Firehose(AWSProperty):
    """
    `Firehose <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-firehose.html>`__
    """

    props: PropsDictType = {
        "DeliveryStream": (str, False),
        "Enabled": (boolean, True),
    }


class S3(AWSProperty):
    """
    `S3 <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-s3.html>`__
    """

    props: PropsDictType = {
        "Bucket": (str, False),
        "Enabled": (boolean, True),
        "Prefix": (str, False),
    }


class BrokerLogs(AWSProperty):
    """
    `BrokerLogs <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokerlogs.html>`__
    """

    props: PropsDictType = {
        "CloudWatchLogs": (CloudWatchLogs, False),
        "Firehose": (Firehose, False),
        "S3": (S3, False),
    }


class LoggingInfo(AWSProperty):
    """
    `LoggingInfo <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-logginginfo.html>`__
    """

    props: PropsDictType = {
        "BrokerLogs": (BrokerLogs, True),
    }


class JmxExporter(AWSProperty):
    """
    `JmxExporter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-jmxexporter.html>`__
    """

    props: PropsDictType = {
        "EnabledInBroker": (boolean, True),
    }


class NodeExporter(AWSProperty):
    """
    `NodeExporter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-nodeexporter.html>`__
    """

    props: PropsDictType = {
        "EnabledInBroker": (boolean, True),
    }


class Prometheus(AWSProperty):
    """
    `Prometheus <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-prometheus.html>`__
    """

    props: PropsDictType = {
        "JmxExporter": (JmxExporter, False),
        "NodeExporter": (NodeExporter, False),
    }


class OpenMonitoring(AWSProperty):
    """
    `OpenMonitoring <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-openmonitoring.html>`__
    """

    props: PropsDictType = {
        "Prometheus": (Prometheus, True),
    }


class Cluster(AWSObject):
    """
    `Cluster <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html>`__
    """

    resource_type = "AWS::MSK::Cluster"

    props: PropsDictType = {
        "BrokerNodeGroupInfo": (BrokerNodeGroupInfo, True),
        "ClientAuthentication": (ClientAuthentication, False),
        "ClusterName": (str, True),
        "ConfigurationInfo": (ConfigurationInfo, False),
        "CurrentVersion": (str, False),
        "EncryptionInfo": (EncryptionInfo, False),
        "EnhancedMonitoring": (str, False),
        "KafkaVersion": (str, True),
        "LoggingInfo": (LoggingInfo, False),
        "NumberOfBrokerNodes": (integer, True),
        "OpenMonitoring": (OpenMonitoring, False),
        "StorageMode": (str, False),
        "Tags": (dict, False),
    }


class ClusterPolicy(AWSObject):
    """
    `ClusterPolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-clusterpolicy.html>`__
    """

    resource_type = "AWS::MSK::ClusterPolicy"

    props: PropsDictType = {
        "ClusterArn": (str, True),
        "Policy": (dict, True),
    }


class LatestRevision(AWSProperty):
    """
    `LatestRevision <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-configuration-latestrevision.html>`__
    """

    props: PropsDictType = {
        "CreationTime": (str, False),
        "Description": (str, False),
        "Revision": (integer, False),
    }


class Configuration(AWSObject):
    """
    `Configuration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-configuration.html>`__
    """

    resource_type = "AWS::MSK::Configuration"

    props: PropsDictType = {
        "Description": (str, False),
        "KafkaVersionsList": ([str], False),
        "LatestRevision": (LatestRevision, False),
        "Name": (str, True),
        "ServerProperties": (str, True),
    }


class AmazonMskCluster(AWSProperty):
    """
    `AmazonMskCluster <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-replicator-amazonmskcluster.html>`__
    """

    props: PropsDictType = {
        "MskClusterArn": (str, True),
    }


class KafkaClusterClientVpcConfig(AWSProperty):
    """
    `KafkaClusterClientVpcConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-replicator-kafkaclusterclientvpcconfig.html>`__
    """

    props: PropsDictType = {
        "SecurityGroupIds": ([str], False),
        "SubnetIds": ([str], True),
    }


class KafkaCluster(AWSProperty):
    """
    `KafkaCluster <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-replicator-kafkacluster.html>`__
    """

    props: PropsDictType = {
        "AmazonMskCluster": (AmazonMskCluster, True),
        "VpcConfig": (KafkaClusterClientVpcConfig, True),
    }


class ConsumerGroupReplication(AWSProperty):
    """
    `ConsumerGroupReplication <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-replicator-consumergroupreplication.html>`__
    """

    props: PropsDictType = {
        "ConsumerGroupsToExclude": ([str], False),
        "ConsumerGroupsToReplicate": ([str], True),
        "DetectAndCopyNewConsumerGroups": (boolean, False),
        "SynchroniseConsumerGroupOffsets": (boolean, False),
    }


class ReplicationStartingPosition(AWSProperty):
    """
    `ReplicationStartingPosition <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-replicator-replicationstartingposition.html>`__
    """

    props: PropsDictType = {
        "Type": (str, False),
    }


class ReplicationTopicNameConfiguration(AWSProperty):
    """
    `ReplicationTopicNameConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-replicator-replicationtopicnameconfiguration.html>`__
    """

    props: PropsDictType = {
        "Type": (str, False),
    }


class TopicReplication(AWSProperty):
    """
    `TopicReplication <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-replicator-topicreplication.html>`__
    """

    props: PropsDictType = {
        "CopyAccessControlListsForTopics": (boolean, False),
        "CopyTopicConfigurations": (boolean, False),
        "DetectAndCopyNewTopics": (boolean, False),
        "StartingPosition": (ReplicationStartingPosition, False),
        "TopicNameConfiguration": (ReplicationTopicNameConfiguration, False),
        "TopicsToExclude": ([str], False),
        "TopicsToReplicate": ([str], True),
    }


class ReplicationInfo(AWSProperty):
    """
    `ReplicationInfo <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-replicator-replicationinfo.html>`__
    """

    props: PropsDictType = {
        "ConsumerGroupReplication": (ConsumerGroupReplication, True),
        "SourceKafkaClusterArn": (str, True),
        "TargetCompressionType": (str, True),
        "TargetKafkaClusterArn": (str, True),
        "TopicReplication": (TopicReplication, True),
    }


class Replicator(AWSObject):
    """
    `Replicator <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-replicator.html>`__
    """

    resource_type = "AWS::MSK::Replicator"

    props: PropsDictType = {
        "CurrentVersion": (str, False),
        "Description": (str, False),
        "KafkaClusters": ([KafkaCluster], True),
        "ReplicationInfoList": ([ReplicationInfo], True),
        "ReplicatorName": (str, True),
        "ServiceExecutionRoleArn": (str, True),
        "Tags": (Tags, False),
    }


class VpcConfig(AWSProperty):
    """
    `VpcConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-serverlesscluster-vpcconfig.html>`__
    """

    props: PropsDictType = {
        "SecurityGroups": ([str], False),
        "SubnetIds": ([str], True),
    }


class ServerlessCluster(AWSObject):
    """
    `ServerlessCluster <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-serverlesscluster.html>`__
    """

    resource_type = "AWS::MSK::ServerlessCluster"

    props: PropsDictType = {
        "ClientAuthentication": (ClientAuthentication, True),
        "ClusterName": (str, True),
        "Tags": (dict, False),
        "VpcConfigs": ([VpcConfig], True),
    }


class VpcConnection(AWSObject):
    """
    `VpcConnection <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-vpcconnection.html>`__
    """

    resource_type = "AWS::MSK::VpcConnection"

    props: PropsDictType = {
        "Authentication": (str, True),
        "ClientSubnets": ([str], True),
        "SecurityGroups": ([str], True),
        "Tags": (dict, False),
        "TargetClusterArn": (str, True),
        "VpcId": (str, True),
    }