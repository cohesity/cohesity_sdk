"""
    Cohesity REST API

    Cohesity API provides a RESTful interface to access the various data management operations on Cohesity cluster and Helios.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from cohesity_sdk.cohesity_client_v2.model_utils import (  # noqa: F401
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
    from cohesity_sdk.cohesity_client_v2.model.archival_data_stats import ArchivalDataStats
    from cohesity_sdk.cohesity_client_v2.model.data_lock_constraints import DataLockConstraints
    globals()['ArchivalDataStats'] = ArchivalDataStats
    globals()['DataLockConstraints'] = DataLockConstraints


class ArchivalTargetResultAllOf(ModelNormal):
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
        ('run_type',): {
            'None': None,
            'KREGULAR': "kRegular",
            'KFULL': "kFull",
            'KLOG': "kLog",
            'KSYSTEM': "kSystem",
            'KHYDRATECDP': "kHydrateCDP",
        },
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
            'PAUSED': "Paused",
            'PAUSING': "Pausing",
            'RESUMING': "Resuming",
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
            'run_type': (str, none_type,),  # noqa: E501
            'is_sla_violated': (bool, none_type,),  # noqa: E501
            'snapshot_id': (str, none_type,),  # noqa: E501
            'start_time_usecs': (int, none_type,),  # noqa: E501
            'end_time_usecs': (int, none_type,),  # noqa: E501
            'queued_time_usecs': (int, none_type,),  # noqa: E501
            'is_incremental': (bool, none_type,),  # noqa: E501
            'is_forever_incremental': (bool, none_type,),  # noqa: E501
            'status': (str, none_type,),  # noqa: E501
            'message': (str, none_type,),  # noqa: E501
            'progress_task_id': (str, none_type,),  # noqa: E501
            'indexing_task_id': (str, none_type,),  # noqa: E501
            'successful_objects_count': (int, none_type,),  # noqa: E501
            'failed_objects_count': (int, none_type,),  # noqa: E501
            'cancelled_objects_count': (int, none_type,),  # noqa: E501
            'successful_app_objects_count': (int, none_type,),  # noqa: E501
            'failed_app_objects_count': (int, none_type,),  # noqa: E501
            'cancelled_app_objects_count': (int, none_type,),  # noqa: E501
            'stats': (ArchivalDataStats,),  # noqa: E501
            'is_manually_deleted': (bool, none_type,),  # noqa: E501
            'expiry_time_usecs': (int, none_type,),  # noqa: E501
            'data_lock_constraints': (DataLockConstraints,),  # noqa: E501
            'on_legal_hold': (bool, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None



    attribute_map = {
        'run_type': 'runType',  # noqa: E501
        'is_sla_violated': 'isSlaViolated',  # noqa: E501
        'snapshot_id': 'snapshotId',  # noqa: E501
        'start_time_usecs': 'startTimeUsecs',  # noqa: E501
        'end_time_usecs': 'endTimeUsecs',  # noqa: E501
        'queued_time_usecs': 'queuedTimeUsecs',  # noqa: E501
        'is_incremental': 'isIncremental',  # noqa: E501
        'is_forever_incremental': 'isForeverIncremental',  # noqa: E501
        'status': 'status',  # noqa: E501
        'message': 'message',  # noqa: E501
        'progress_task_id': 'progressTaskId',  # noqa: E501
        'indexing_task_id': 'indexingTaskId',  # noqa: E501
        'successful_objects_count': 'successfulObjectsCount',  # noqa: E501
        'failed_objects_count': 'failedObjectsCount',  # noqa: E501
        'cancelled_objects_count': 'cancelledObjectsCount',  # noqa: E501
        'successful_app_objects_count': 'successfulAppObjectsCount',  # noqa: E501
        'failed_app_objects_count': 'failedAppObjectsCount',  # noqa: E501
        'cancelled_app_objects_count': 'cancelledAppObjectsCount',  # noqa: E501
        'stats': 'stats',  # noqa: E501
        'is_manually_deleted': 'isManuallyDeleted',  # noqa: E501
        'expiry_time_usecs': 'expiryTimeUsecs',  # noqa: E501
        'data_lock_constraints': 'dataLockConstraints',  # noqa: E501
        'on_legal_hold': 'onLegalHold',  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """ArchivalTargetResultAllOf - a model defined in OpenAPI

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

            run_type (str, none_type): Type of Protection Group run. 'kRegular' indicates an incremental (CBT) backup. Incremental backups utilizing CBT (if supported) are captured of the target protection objects. The first run of a kRegular schedule captures all the blocks. 'kFull' indicates a full (no CBT) backup. A complete backup (all blocks) of the target protection objects are always captured and Change Block Tracking (CBT) is not utilized. 'kLog' indicates a Database Log backup. Capture the database transaction logs to allow rolling back to a specific point in time. 'kSystem' indicates system volume backup. It produces an image for bare metal recovery.. [optional]  # noqa: E501
            is_sla_violated (bool, none_type): Indicated if SLA has been violated for this run.. [optional]  # noqa: E501
            snapshot_id (str, none_type): Snapshot id for a successful snapshot. This field will not be set if the archival Run fails to take the snapshot.. [optional]  # noqa: E501
            start_time_usecs (int, none_type): Specifies the start time of replication run in Unix epoch Timestamp(in microseconds) for an archival target.. [optional]  # noqa: E501
            end_time_usecs (int, none_type): Specifies the end time of replication run in Unix epoch Timestamp(in microseconds) for an archival target.. [optional]  # noqa: E501
            queued_time_usecs (int, none_type): Specifies the time when the archival is queued for schedule in Unix epoch Timestamp(in microseconds) for a target.. [optional]  # noqa: E501
            is_incremental (bool, none_type): Whether this is an incremental archive. If set to true, this is an incremental archive, otherwise this is a full archive.. [optional]  # noqa: E501
            is_forever_incremental (bool, none_type): Whether this is forever incremental or not. [optional]  # noqa: E501
            status (str, none_type): Status of the replication run for an archival target. 'Running' indicates that the run is still running. 'Canceled' indicates that the run has been canceled. 'Canceling' indicates that the run is in the process of being canceled. 'Paused' indicates that the ongoing run has been paused. 'Failed' indicates that the run has failed. 'Missed' indicates that the run was unable to take place at the scheduled time because the previous run was still happening. 'Succeeded' indicates that the run has finished successfully. 'SucceededWithWarning' indicates that the run finished successfully, but there were some warning messages.. [optional]  # noqa: E501
            message (str, none_type): Message about the archival run.. [optional]  # noqa: E501
            progress_task_id (str, none_type): Progress monitor task id for archival.. [optional]  # noqa: E501
            indexing_task_id (str, none_type): Progress monitor task for indexing.. [optional]  # noqa: E501
            successful_objects_count (int, none_type): Specifies the count of objects for which backup was successful.. [optional]  # noqa: E501
            failed_objects_count (int, none_type): Specifies the count of objects for which backup failed.. [optional]  # noqa: E501
            cancelled_objects_count (int, none_type): Specifies the count of objects for which backup was cancelled.. [optional]  # noqa: E501
            successful_app_objects_count (int, none_type): Specifies the count of app objects for which backup was successful.. [optional]  # noqa: E501
            failed_app_objects_count (int, none_type): Specifies the count of app objects for which backup failed.. [optional]  # noqa: E501
            cancelled_app_objects_count (int, none_type): Specifies the count of app objects for which backup was cancelled.. [optional]  # noqa: E501
            stats (ArchivalDataStats): [optional]  # noqa: E501
            is_manually_deleted (bool, none_type): Specifies whether the snapshot is deleted manually.. [optional]  # noqa: E501
            expiry_time_usecs (int, none_type): Specifies the expiry time of attempt in Unix epoch Timestamp (in microseconds).. [optional]  # noqa: E501
            data_lock_constraints (DataLockConstraints): [optional]  # noqa: E501
            on_legal_hold (bool, none_type): Specifies the legal hold status for a archival target.. [optional]  # noqa: E501
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


        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)


