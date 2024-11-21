# Copyright (c) 2012-2024, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType
from .validators import boolean, double, integer


class ScalableTargetAction(AWSProperty):
    """
    `ScalableTargetAction <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-scalabletargetaction.html>`__
    """

    props: PropsDictType = {
        "MaxCapacity": (integer, False),
        "MinCapacity": (integer, False),
    }


class ScheduledAction(AWSProperty):
    """
    `ScheduledAction <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-scheduledaction.html>`__
    """

    props: PropsDictType = {
        "EndTime": (str, False),
        "ScalableTargetAction": (ScalableTargetAction, False),
        "Schedule": (str, True),
        "ScheduledActionName": (str, True),
        "StartTime": (str, False),
        "Timezone": (str, False),
    }


class SuspendedState(AWSProperty):
    """
    `SuspendedState <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-suspendedstate.html>`__
    """

    props: PropsDictType = {
        "DynamicScalingInSuspended": (boolean, False),
        "DynamicScalingOutSuspended": (boolean, False),
        "ScheduledScalingSuspended": (boolean, False),
    }


class ScalableTarget(AWSObject):
    """
    `ScalableTarget <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html>`__
    """

    resource_type = "AWS::ApplicationAutoScaling::ScalableTarget"

    props: PropsDictType = {
        "MaxCapacity": (integer, True),
        "MinCapacity": (integer, True),
        "ResourceId": (str, True),
        "RoleARN": (str, False),
        "ScalableDimension": (str, True),
        "ScheduledActions": ([ScheduledAction], False),
        "ServiceNamespace": (str, True),
        "SuspendedState": (SuspendedState, False),
    }


class StepAdjustment(AWSProperty):
    """
    `StepAdjustment <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepadjustment.html>`__
    """

    props: PropsDictType = {
        "MetricIntervalLowerBound": (double, False),
        "MetricIntervalUpperBound": (double, False),
        "ScalingAdjustment": (integer, True),
    }


class StepScalingPolicyConfiguration(AWSProperty):
    """
    `StepScalingPolicyConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration.html>`__
    """

    props: PropsDictType = {
        "AdjustmentType": (str, False),
        "Cooldown": (integer, False),
        "MetricAggregationType": (str, False),
        "MinAdjustmentMagnitude": (integer, False),
        "StepAdjustments": ([StepAdjustment], False),
    }


class MetricDimension(AWSProperty):
    """
    `MetricDimension <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-metricdimension.html>`__
    """

    props: PropsDictType = {
        "Name": (str, True),
        "Value": (str, True),
    }


class TargetTrackingMetricDimension(AWSProperty):
    """
    `TargetTrackingMetricDimension <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetricdimension.html>`__
    """

    props: PropsDictType = {
        "Name": (str, False),
        "Value": (str, False),
    }


class TargetTrackingMetric(AWSProperty):
    """
    `TargetTrackingMetric <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetric.html>`__
    """

    props: PropsDictType = {
        "Dimensions": ([TargetTrackingMetricDimension], False),
        "MetricName": (str, False),
        "Namespace": (str, False),
    }


class TargetTrackingMetricStat(AWSProperty):
    """
    `TargetTrackingMetricStat <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetricstat.html>`__
    """

    props: PropsDictType = {
        "Metric": (TargetTrackingMetric, False),
        "Stat": (str, False),
        "Unit": (str, False),
    }


class TargetTrackingMetricDataQuery(AWSProperty):
    """
    `TargetTrackingMetricDataQuery <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetricdataquery.html>`__
    """

    props: PropsDictType = {
        "Expression": (str, False),
        "Id": (str, False),
        "Label": (str, False),
        "MetricStat": (TargetTrackingMetricStat, False),
        "ReturnData": (boolean, False),
    }


class CustomizedMetricSpecification(AWSProperty):
    """
    `CustomizedMetricSpecification <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-customizedmetricspecification.html>`__
    """

    props: PropsDictType = {
        "Dimensions": ([MetricDimension], False),
        "MetricName": (str, False),
        "Metrics": ([TargetTrackingMetricDataQuery], False),
        "Namespace": (str, False),
        "Statistic": (str, False),
        "Unit": (str, False),
    }


class PredefinedMetricSpecification(AWSProperty):
    """
    `PredefinedMetricSpecification <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-predefinedmetricspecification.html>`__
    """

    props: PropsDictType = {
        "PredefinedMetricType": (str, True),
        "ResourceLabel": (str, False),
    }


class TargetTrackingScalingPolicyConfiguration(AWSProperty):
    """
    `TargetTrackingScalingPolicyConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration.html>`__
    """

    props: PropsDictType = {
        "CustomizedMetricSpecification": (CustomizedMetricSpecification, False),
        "DisableScaleIn": (boolean, False),
        "PredefinedMetricSpecification": (PredefinedMetricSpecification, False),
        "ScaleInCooldown": (integer, False),
        "ScaleOutCooldown": (integer, False),
        "TargetValue": (double, True),
    }


class ScalingPolicy(AWSObject):
    """
    `ScalingPolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html>`__
    """

    resource_type = "AWS::ApplicationAutoScaling::ScalingPolicy"

    props: PropsDictType = {
        "PolicyName": (str, True),
        "PolicyType": (str, True),
        "ResourceId": (str, False),
        "ScalableDimension": (str, False),
        "ScalingTargetId": (str, False),
        "ServiceNamespace": (str, False),
        "StepScalingPolicyConfiguration": (StepScalingPolicyConfiguration, False),
        "TargetTrackingScalingPolicyConfiguration": (
            TargetTrackingScalingPolicyConfiguration,
            False,
        ),
    }
