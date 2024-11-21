# Copyright (c) 2012-2024, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType
from .validators import boolean, double


class ReferenceItem(AWSProperty):
    """
    `ReferenceItem <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-variantstore-referenceitem.html>`__
    """

    props: PropsDictType = {
        "ReferenceArn": (str, True),
    }


class SseConfig(AWSProperty):
    """
    `SseConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-variantstore-sseconfig.html>`__
    """

    props: PropsDictType = {
        "KeyArn": (str, False),
        "Type": (str, True),
    }


class TsvStoreOptions(AWSProperty):
    """
    `TsvStoreOptions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-annotationstore-tsvstoreoptions.html>`__
    """

    props: PropsDictType = {
        "AnnotationType": (str, False),
        "FormatToHeader": (dict, False),
        "Schema": (dict, False),
    }


class StoreOptions(AWSProperty):
    """
    `StoreOptions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-annotationstore-storeoptions.html>`__
    """

    props: PropsDictType = {
        "TsvStoreOptions": (TsvStoreOptions, True),
    }


class AnnotationStore(AWSObject):
    """
    `AnnotationStore <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-annotationstore.html>`__
    """

    resource_type = "AWS::Omics::AnnotationStore"

    props: PropsDictType = {
        "Description": (str, False),
        "Name": (str, True),
        "Reference": (ReferenceItem, False),
        "SseConfig": (SseConfig, False),
        "StoreFormat": (str, True),
        "StoreOptions": (StoreOptions, False),
        "Tags": (dict, False),
    }


class ReferenceStore(AWSObject):
    """
    `ReferenceStore <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-referencestore.html>`__
    """

    resource_type = "AWS::Omics::ReferenceStore"

    props: PropsDictType = {
        "Description": (str, False),
        "Name": (str, True),
        "SseConfig": (SseConfig, False),
        "Tags": (dict, False),
    }


class RunGroup(AWSObject):
    """
    `RunGroup <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-rungroup.html>`__
    """

    resource_type = "AWS::Omics::RunGroup"

    props: PropsDictType = {
        "MaxCpus": (double, False),
        "MaxDuration": (double, False),
        "MaxGpus": (double, False),
        "MaxRuns": (double, False),
        "Name": (str, False),
        "Tags": (dict, False),
    }


class SequenceStore(AWSObject):
    """
    `SequenceStore <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-sequencestore.html>`__
    """

    resource_type = "AWS::Omics::SequenceStore"

    props: PropsDictType = {
        "Description": (str, False),
        "FallbackLocation": (str, False),
        "Name": (str, True),
        "SseConfig": (SseConfig, False),
        "Tags": (dict, False),
    }


class VariantStore(AWSObject):
    """
    `VariantStore <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-variantstore.html>`__
    """

    resource_type = "AWS::Omics::VariantStore"

    props: PropsDictType = {
        "Description": (str, False),
        "Name": (str, True),
        "Reference": (ReferenceItem, True),
        "SseConfig": (SseConfig, False),
        "Tags": (dict, False),
    }


class WorkflowParameter(AWSProperty):
    """
    `WorkflowParameter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-workflow-workflowparameter.html>`__
    """

    props: PropsDictType = {
        "Description": (str, False),
        "Optional": (boolean, False),
    }


class Workflow(AWSObject):
    """
    `Workflow <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-workflow.html>`__
    """

    resource_type = "AWS::Omics::Workflow"

    props: PropsDictType = {
        "Accelerators": (str, False),
        "DefinitionUri": (str, False),
        "Description": (str, False),
        "Engine": (str, False),
        "Main": (str, False),
        "Name": (str, False),
        "ParameterTemplate": (dict, False),
        "StorageCapacity": (double, False),
        "Tags": (dict, False),
    }
