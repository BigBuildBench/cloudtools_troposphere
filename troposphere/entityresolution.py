# Copyright (c) 2012-2024, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean


class Rule(AWSProperty):
    """
    `Rule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-matchingworkflow-rule.html>`__
    """

    props: PropsDictType = {
        "MatchingKeys": ([str], True),
        "RuleName": (str, True),
    }


class IdMappingRuleBasedProperties(AWSProperty):
    """
    `IdMappingRuleBasedProperties <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-idmappingworkflow-idmappingrulebasedproperties.html>`__
    """

    props: PropsDictType = {
        "AttributeMatchingModel": (str, True),
        "RecordMatchingModel": (str, True),
        "RuleDefinitionType": (str, False),
        "Rules": ([Rule], False),
    }


class IntermediateSourceConfiguration(AWSProperty):
    """
    `IntermediateSourceConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-matchingworkflow-intermediatesourceconfiguration.html>`__
    """

    props: PropsDictType = {
        "IntermediateS3Path": (str, True),
    }


class ProviderProperties(AWSProperty):
    """
    `ProviderProperties <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-matchingworkflow-providerproperties.html>`__
    """

    props: PropsDictType = {
        "IntermediateSourceConfiguration": (IntermediateSourceConfiguration, False),
        "ProviderConfiguration": (dict, False),
        "ProviderServiceArn": (str, True),
    }


class IdMappingTechniques(AWSProperty):
    """
    `IdMappingTechniques <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-idmappingworkflow-idmappingtechniques.html>`__
    """

    props: PropsDictType = {
        "IdMappingType": (str, False),
        "ProviderProperties": (ProviderProperties, False),
        "RuleBasedProperties": (IdMappingRuleBasedProperties, False),
    }


class IdMappingWorkflowInputSource(AWSProperty):
    """
    `IdMappingWorkflowInputSource <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-idmappingworkflow-idmappingworkflowinputsource.html>`__
    """

    props: PropsDictType = {
        "InputSourceARN": (str, True),
        "SchemaArn": (str, False),
        "Type": (str, False),
    }


class IdMappingWorkflowOutputSource(AWSProperty):
    """
    `IdMappingWorkflowOutputSource <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-idmappingworkflow-idmappingworkflowoutputsource.html>`__
    """

    props: PropsDictType = {
        "KMSArn": (str, False),
        "OutputS3Path": (str, True),
    }


class IdMappingWorkflow(AWSObject):
    """
    `IdMappingWorkflow <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-entityresolution-idmappingworkflow.html>`__
    """

    resource_type = "AWS::EntityResolution::IdMappingWorkflow"

    props: PropsDictType = {
        "Description": (str, False),
        "IdMappingTechniques": (IdMappingTechniques, True),
        "InputSourceConfig": ([IdMappingWorkflowInputSource], True),
        "OutputSourceConfig": ([IdMappingWorkflowOutputSource], False),
        "RoleArn": (str, True),
        "Tags": (Tags, False),
        "WorkflowName": (str, True),
    }


class NamespaceProviderProperties(AWSProperty):
    """
    `NamespaceProviderProperties <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-idnamespace-namespaceproviderproperties.html>`__
    """

    props: PropsDictType = {
        "ProviderConfiguration": (dict, False),
        "ProviderServiceArn": (str, True),
    }


class NamespaceRuleBasedProperties(AWSProperty):
    """
    `NamespaceRuleBasedProperties <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-idnamespace-namespacerulebasedproperties.html>`__
    """

    props: PropsDictType = {
        "AttributeMatchingModel": (str, False),
        "RecordMatchingModels": ([str], False),
        "RuleDefinitionTypes": ([str], False),
        "Rules": ([Rule], False),
    }


class IdNamespaceIdMappingWorkflowProperties(AWSProperty):
    """
    `IdNamespaceIdMappingWorkflowProperties <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-idnamespace-idnamespaceidmappingworkflowproperties.html>`__
    """

    props: PropsDictType = {
        "IdMappingType": (str, True),
        "ProviderProperties": (NamespaceProviderProperties, False),
        "RuleBasedProperties": (NamespaceRuleBasedProperties, False),
    }


class IdNamespaceInputSource(AWSProperty):
    """
    `IdNamespaceInputSource <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-idnamespace-idnamespaceinputsource.html>`__
    """

    props: PropsDictType = {
        "InputSourceARN": (str, True),
        "SchemaName": (str, False),
    }


class IdNamespace(AWSObject):
    """
    `IdNamespace <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-entityresolution-idnamespace.html>`__
    """

    resource_type = "AWS::EntityResolution::IdNamespace"

    props: PropsDictType = {
        "Description": (str, False),
        "IdMappingWorkflowProperties": (
            [IdNamespaceIdMappingWorkflowProperties],
            False,
        ),
        "IdNamespaceName": (str, True),
        "InputSourceConfig": ([IdNamespaceInputSource], False),
        "RoleArn": (str, False),
        "Tags": (Tags, False),
        "Type": (str, True),
    }


class IncrementalRunConfig(AWSProperty):
    """
    `IncrementalRunConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-matchingworkflow-incrementalrunconfig.html>`__
    """

    props: PropsDictType = {
        "IncrementalRunType": (str, True),
    }


class InputSource(AWSProperty):
    """
    `InputSource <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-matchingworkflow-inputsource.html>`__
    """

    props: PropsDictType = {
        "ApplyNormalization": (boolean, False),
        "InputSourceARN": (str, True),
        "SchemaArn": (str, True),
    }


class OutputAttribute(AWSProperty):
    """
    `OutputAttribute <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-matchingworkflow-outputattribute.html>`__
    """

    props: PropsDictType = {
        "Hashed": (boolean, False),
        "Name": (str, True),
    }


class OutputSource(AWSProperty):
    """
    `OutputSource <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-matchingworkflow-outputsource.html>`__
    """

    props: PropsDictType = {
        "ApplyNormalization": (boolean, False),
        "KMSArn": (str, False),
        "Output": ([OutputAttribute], True),
        "OutputS3Path": (str, True),
    }


class RuleBasedProperties(AWSProperty):
    """
    `RuleBasedProperties <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-matchingworkflow-rulebasedproperties.html>`__
    """

    props: PropsDictType = {
        "AttributeMatchingModel": (str, True),
        "MatchPurpose": (str, False),
        "Rules": ([Rule], True),
    }


class ResolutionTechniques(AWSProperty):
    """
    `ResolutionTechniques <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-matchingworkflow-resolutiontechniques.html>`__
    """

    props: PropsDictType = {
        "ProviderProperties": (ProviderProperties, False),
        "ResolutionType": (str, False),
        "RuleBasedProperties": (RuleBasedProperties, False),
    }


class MatchingWorkflow(AWSObject):
    """
    `MatchingWorkflow <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-entityresolution-matchingworkflow.html>`__
    """

    resource_type = "AWS::EntityResolution::MatchingWorkflow"

    props: PropsDictType = {
        "Description": (str, False),
        "IncrementalRunConfig": (IncrementalRunConfig, False),
        "InputSourceConfig": ([InputSource], True),
        "OutputSourceConfig": ([OutputSource], True),
        "ResolutionTechniques": (ResolutionTechniques, True),
        "RoleArn": (str, True),
        "Tags": (Tags, False),
        "WorkflowName": (str, True),
    }


class PolicyStatement(AWSObject):
    """
    `PolicyStatement <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-entityresolution-policystatement.html>`__
    """

    resource_type = "AWS::EntityResolution::PolicyStatement"

    props: PropsDictType = {
        "Action": ([str], False),
        "Arn": (str, True),
        "Condition": (str, False),
        "Effect": (str, False),
        "Principal": ([str], False),
        "StatementId": (str, True),
    }


class SchemaInputAttribute(AWSProperty):
    """
    `SchemaInputAttribute <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-schemamapping-schemainputattribute.html>`__
    """

    props: PropsDictType = {
        "FieldName": (str, True),
        "GroupName": (str, False),
        "Hashed": (boolean, False),
        "MatchKey": (str, False),
        "SubType": (str, False),
        "Type": (str, True),
    }


class SchemaMapping(AWSObject):
    """
    `SchemaMapping <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-entityresolution-schemamapping.html>`__
    """

    resource_type = "AWS::EntityResolution::SchemaMapping"

    props: PropsDictType = {
        "Description": (str, False),
        "MappedInputFields": ([SchemaInputAttribute], True),
        "SchemaName": (str, True),
        "Tags": (Tags, False),
    }