# Copyright (c) 2012-2024, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, integer


class AccessLogSubscription(AWSObject):
    """
    `AccessLogSubscription <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-accesslogsubscription.html>`__
    """

    resource_type = "AWS::VpcLattice::AccessLogSubscription"

    props: PropsDictType = {
        "DestinationArn": (str, True),
        "ResourceIdentifier": (str, False),
        "Tags": (Tags, False),
    }


class AuthPolicy(AWSObject):
    """
    `AuthPolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-authpolicy.html>`__
    """

    resource_type = "AWS::VpcLattice::AuthPolicy"

    props: PropsDictType = {
        "Policy": (dict, True),
        "ResourceIdentifier": (str, True),
    }


class FixedResponse(AWSProperty):
    """
    `FixedResponse <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-rule-fixedresponse.html>`__
    """

    props: PropsDictType = {
        "StatusCode": (integer, True),
    }


class WeightedTargetGroup(AWSProperty):
    """
    `WeightedTargetGroup <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-rule-weightedtargetgroup.html>`__
    """

    props: PropsDictType = {
        "TargetGroupIdentifier": (str, True),
        "Weight": (integer, False),
    }


class Forward(AWSProperty):
    """
    `Forward <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-rule-forward.html>`__
    """

    props: PropsDictType = {
        "TargetGroups": ([WeightedTargetGroup], True),
    }


class DefaultAction(AWSProperty):
    """
    `DefaultAction <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-listener-defaultaction.html>`__
    """

    props: PropsDictType = {
        "FixedResponse": (FixedResponse, False),
        "Forward": (Forward, False),
    }


class Listener(AWSObject):
    """
    `Listener <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-listener.html>`__
    """

    resource_type = "AWS::VpcLattice::Listener"

    props: PropsDictType = {
        "DefaultAction": (DefaultAction, True),
        "Name": (str, False),
        "Port": (integer, False),
        "Protocol": (str, True),
        "ServiceIdentifier": (str, False),
        "Tags": (Tags, False),
    }


class ResourcePolicy(AWSObject):
    """
    `ResourcePolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-resourcepolicy.html>`__
    """

    resource_type = "AWS::VpcLattice::ResourcePolicy"

    props: PropsDictType = {
        "Policy": (dict, True),
        "ResourceArn": (str, True),
    }


class Action(AWSProperty):
    """
    `Action <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-rule-action.html>`__
    """

    props: PropsDictType = {
        "FixedResponse": (FixedResponse, False),
        "Forward": (Forward, False),
    }


class HeaderMatchType(AWSProperty):
    """
    `HeaderMatchType <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-rule-headermatchtype.html>`__
    """

    props: PropsDictType = {
        "Contains": (str, False),
        "Exact": (str, False),
        "Prefix": (str, False),
    }


class HeaderMatch(AWSProperty):
    """
    `HeaderMatch <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-rule-headermatch.html>`__
    """

    props: PropsDictType = {
        "CaseSensitive": (boolean, False),
        "Match": (HeaderMatchType, True),
        "Name": (str, True),
    }


class PathMatchType(AWSProperty):
    """
    `PathMatchType <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-rule-pathmatchtype.html>`__
    """

    props: PropsDictType = {
        "Exact": (str, False),
        "Prefix": (str, False),
    }


class PathMatch(AWSProperty):
    """
    `PathMatch <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-rule-pathmatch.html>`__
    """

    props: PropsDictType = {
        "CaseSensitive": (boolean, False),
        "Match": (PathMatchType, True),
    }


class HttpMatch(AWSProperty):
    """
    `HttpMatch <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-rule-httpmatch.html>`__
    """

    props: PropsDictType = {
        "HeaderMatches": ([HeaderMatch], False),
        "Method": (str, False),
        "PathMatch": (PathMatch, False),
    }


class Match(AWSProperty):
    """
    `Match <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-rule-match.html>`__
    """

    props: PropsDictType = {
        "HttpMatch": (HttpMatch, True),
    }


class Rule(AWSObject):
    """
    `Rule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-rule.html>`__
    """

    resource_type = "AWS::VpcLattice::Rule"

    props: PropsDictType = {
        "Action": (Action, True),
        "ListenerIdentifier": (str, False),
        "Match": (Match, True),
        "Name": (str, False),
        "Priority": (integer, True),
        "ServiceIdentifier": (str, False),
        "Tags": (Tags, False),
    }


class DnsEntry(AWSProperty):
    """
    `DnsEntry <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-servicenetworkserviceassociation-dnsentry.html>`__
    """

    props: PropsDictType = {
        "DomainName": (str, False),
        "HostedZoneId": (str, False),
    }


class Service(AWSObject):
    """
    `Service <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-service.html>`__
    """

    resource_type = "AWS::VpcLattice::Service"

    props: PropsDictType = {
        "AuthType": (str, False),
        "CertificateArn": (str, False),
        "CustomDomainName": (str, False),
        "DnsEntry": (DnsEntry, False),
        "Name": (str, False),
        "Tags": (Tags, False),
    }


class ServiceNetwork(AWSObject):
    """
    `ServiceNetwork <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-servicenetwork.html>`__
    """

    resource_type = "AWS::VpcLattice::ServiceNetwork"

    props: PropsDictType = {
        "AuthType": (str, False),
        "Name": (str, False),
        "Tags": (Tags, False),
    }


class ServiceNetworkServiceAssociation(AWSObject):
    """
    `ServiceNetworkServiceAssociation <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-servicenetworkserviceassociation.html>`__
    """

    resource_type = "AWS::VpcLattice::ServiceNetworkServiceAssociation"

    props: PropsDictType = {
        "DnsEntry": (DnsEntry, False),
        "ServiceIdentifier": (str, False),
        "ServiceNetworkIdentifier": (str, False),
        "Tags": (Tags, False),
    }


class ServiceNetworkVpcAssociation(AWSObject):
    """
    `ServiceNetworkVpcAssociation <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-servicenetworkvpcassociation.html>`__
    """

    resource_type = "AWS::VpcLattice::ServiceNetworkVpcAssociation"

    props: PropsDictType = {
        "SecurityGroupIds": ([str], False),
        "ServiceNetworkIdentifier": (str, False),
        "Tags": (Tags, False),
        "VpcIdentifier": (str, False),
    }


class Target(AWSProperty):
    """
    `Target <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-targetgroup-target.html>`__
    """

    props: PropsDictType = {
        "Id": (str, True),
        "Port": (integer, False),
    }


class Matcher(AWSProperty):
    """
    `Matcher <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-targetgroup-matcher.html>`__
    """

    props: PropsDictType = {
        "HttpCode": (str, True),
    }


class HealthCheckConfig(AWSProperty):
    """
    `HealthCheckConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-targetgroup-healthcheckconfig.html>`__
    """

    props: PropsDictType = {
        "Enabled": (boolean, False),
        "HealthCheckIntervalSeconds": (integer, False),
        "HealthCheckTimeoutSeconds": (integer, False),
        "HealthyThresholdCount": (integer, False),
        "Matcher": (Matcher, False),
        "Path": (str, False),
        "Port": (integer, False),
        "Protocol": (str, False),
        "ProtocolVersion": (str, False),
        "UnhealthyThresholdCount": (integer, False),
    }


class TargetGroupConfig(AWSProperty):
    """
    `TargetGroupConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-targetgroup-targetgroupconfig.html>`__
    """

    props: PropsDictType = {
        "HealthCheck": (HealthCheckConfig, False),
        "IpAddressType": (str, False),
        "LambdaEventStructureVersion": (str, False),
        "Port": (integer, False),
        "Protocol": (str, False),
        "ProtocolVersion": (str, False),
        "VpcIdentifier": (str, False),
    }


class TargetGroup(AWSObject):
    """
    `TargetGroup <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-targetgroup.html>`__
    """

    resource_type = "AWS::VpcLattice::TargetGroup"

    props: PropsDictType = {
        "Config": (TargetGroupConfig, False),
        "Name": (str, False),
        "Tags": (Tags, False),
        "Targets": ([Target], False),
        "Type": (str, True),
    }
