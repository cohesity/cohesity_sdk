"""
    Cohesity REST API

    Cohesity API provides a RESTful interface to access the various data management operations on Cohesity cluster and Helios.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from cohesity_sdk.cluster.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)

def lazy_import():
    from cohesity_sdk.cluster.model.aws_target_config import AWSTargetConfig
    from cohesity_sdk.cluster.model.azure_target_config import AzureTargetConfig
    from cohesity_sdk.cluster.model.data_lock_constraints import DataLockConstraints
    from cohesity_sdk.cluster.model.replication_data_stats import ReplicationDataStats
    from cohesity_sdk.cluster.model.replication_target_result_all_of import ReplicationTargetResultAllOf
    from cohesity_sdk.cluster.model.replication_target_summary_info import ReplicationTargetSummaryInfo
    globals()['AWSTargetConfig'] = AWSTargetConfig
    globals()['AzureTargetConfig'] = AzureTargetConfig
    globals()['DataLockConstraints'] = DataLockConstraints
    globals()['ReplicationDataStats'] = ReplicationDataStats
    globals()['ReplicationTargetResultAllOf'] = ReplicationTargetResultAllOf
    globals()['ReplicationTargetSummaryInfo'] = ReplicationTargetSummaryInfo


class ReplicationTargetResult(ModelComposed):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.

      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.

    """

    allowed_values = {
        ('status',): {
            'None': None,
            'ACCEPTED': "Accepted",
            'RUNNING': "Running",
            'CANCELED': "Canceled",
            'CANCELING': "Canceling",
            'FAILED': "Failed",
            'MISSED': "Missed",
            'SUCCEEDED': "Succeeded",
            'SUCCEEDEDWITHWARNING': "SucceededWithWarning",
            'ONHOLD': "OnHold",
        },
    }

    validations = {
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'cluster_id': (int, none_type,),  # noqa: E501
            'cluster_incarnation_id': (int, none_type,),  # noqa: E501
            'cluster_name': (str, none_type,),  # noqa: E501
            'aws_target_config': (AWSTargetConfig,),  # noqa: E501
            'azure_target_config': (AzureTargetConfig,),  # noqa: E501
            'start_time_usecs': (int, none_type,),  # noqa: E501
            'end_time_usecs': (int, none_type,),  # noqa: E501
            'queued_time_usecs': (int, none_type,),  # noqa: E501
            'status': (str, none_type,),  # noqa: E501
            'message': (str, none_type,),  # noqa: E501
            'percentage_completed': (int, none_type,),  # noqa: E501
            'stats': (ReplicationDataStats,),  # noqa: E501
            'is_manually_deleted': (bool, none_type,),  # noqa: E501
            'expiry_time_usecs': (int, none_type,),  # noqa: E501
            'replication_task_id': (str, none_type,),  # noqa: E501
            'entries_changed': (int, none_type,),  # noqa: E501
            'is_in_bound': (bool, none_type,),  # noqa: E501
            'data_lock_constraints': (DataLockConstraints,),  # noqa: E501
            'on_legal_hold': (bool, none_type,),  # noqa: E501
            'multi_object_replication': (bool, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None



    attribute_map = {
        'cluster_id': 'clusterId',  # noqa: E501
        'cluster_incarnation_id': 'clusterIncarnationId',  # noqa: E501
        'cluster_name': 'clusterName',  # noqa: E501
        'aws_target_config': 'awsTargetConfig',  # noqa: E501
        'azure_target_config': 'azureTargetConfig',  # noqa: E501
        'start_time_usecs': 'startTimeUsecs',  # noqa: E501
        'end_time_usecs': 'endTimeUsecs',  # noqa: E501
        'queued_time_usecs': 'queuedTimeUsecs',  # noqa: E501
        'status': 'status',  # noqa: E501
        'message': 'message',  # noqa: E501
        'percentage_completed': 'percentageCompleted',  # noqa: E501
        'stats': 'stats',  # noqa: E501
        'is_manually_deleted': 'isManuallyDeleted',  # noqa: E501
        'expiry_time_usecs': 'expiryTimeUsecs',  # noqa: E501
        'replication_task_id': 'replicationTaskId',  # noqa: E501
        'entries_changed': 'entriesChanged',  # noqa: E501
        'is_in_bound': 'isInBound',  # noqa: E501
        'data_lock_constraints': 'dataLockConstraints',  # noqa: E501
        'on_legal_hold': 'onLegalHold',  # noqa: E501
        'multi_object_replication': 'multiObjectReplication',  # noqa: E501
    }

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
        '_composed_instances',
        '_var_name_to_model_instances',
        '_additional_properties_model_instances',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """ReplicationTargetResult - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)

            cluster_id (int, none_type): Specifies the id of the cluster.. [optional]  # noqa: E501
            cluster_incarnation_id (int, none_type): Specifies the incarnation id of the cluster.. [optional]  # noqa: E501
            cluster_name (str, none_type): Specifies the name of the cluster.. [optional]  # noqa: E501
            aws_target_config (AWSTargetConfig): [optional]  # noqa: E501
            azure_target_config (AzureTargetConfig): [optional]  # noqa: E501
            start_time_usecs (int, none_type): Specifies the start time of replication in Unix epoch Timestamp(in microseconds) for a target.. [optional]  # noqa: E501
            end_time_usecs (int, none_type): Specifies the end time of replication in Unix epoch Timestamp(in microseconds) for a target.. [optional]  # noqa: E501
            queued_time_usecs (int, none_type): Specifies the time when the replication is queued for schedule in Unix epoch Timestamp(in microseconds) for a target.. [optional]  # noqa: E501
            status (str, none_type): Status of the replication for a target. 'Running' indicates that the run is still running. 'Canceled' indicates that the run has been canceled. 'Canceling' indicates that the run is in the process of being canceled. 'Failed' indicates that the run has failed. 'Missed' indicates that the run was unable to take place at the scheduled time because the previous run was still happening. 'Succeeded' indicates that the run has finished successfully. 'SucceededWithWarning' indicates that the run finished successfully, but there were some warning messages.. [optional]  # noqa: E501
            message (str, none_type): Message about the replication run.. [optional]  # noqa: E501
            percentage_completed (int, none_type): Specifies the progress in percentage.. [optional]  # noqa: E501
            stats (ReplicationDataStats): [optional]  # noqa: E501
            is_manually_deleted (bool, none_type): Specifies whether the snapshot is deleted manually.. [optional]  # noqa: E501
            expiry_time_usecs (int, none_type): Specifies the expiry time of attempt in Unix epoch Timestamp (in microseconds) for an object.. [optional]  # noqa: E501
            replication_task_id (str, none_type): Task UID for a replication protection run. This is for tasks that are replicated from another cluster.. [optional]  # noqa: E501
            entries_changed (int, none_type): Specifies the number of metadata actions completed during the protection run.. [optional]  # noqa: E501
            is_in_bound (bool, none_type): Specifies the direction of the replication. If the snapshot is replicated to this cluster, then isInBound is true. If the snapshot is replicated from this cluster to another cluster, then isInBound is false.. [optional]  # noqa: E501
            data_lock_constraints (DataLockConstraints): [optional]  # noqa: E501
            on_legal_hold (bool, none_type): Specifies the legal hold status for a replication target.. [optional]  # noqa: E501
            multi_object_replication (bool, none_type): Specifies whether view based replication was used. In this case, the view containing all objects is replicated as a whole instead of replicating on a per object basis.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)


        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        required_args = {
        }
        model_args = {}
        model_args.update(required_args)
        model_args.update(kwargs)
        composed_info = validate_get_composed_info(
            constant_args, model_args, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        unused_args = composed_info[3]

        for var_name, var_value in required_args.items():
            setattr(self, var_name, var_value)
        for var_name, var_value in kwargs.items():
            if var_name in unused_args and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        not self._additional_properties_model_instances:
                # discard variable.
                continue
            setattr(self, var_name, var_value)


    @cached_property
    def _composed_schemas():
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error beause the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        lazy_import()
        return {
          'anyOf': [
          ],
          'allOf': [
              ReplicationTargetResultAllOf,
              ReplicationTargetSummaryInfo,
          ],
          'oneOf': [
          ],
        }

