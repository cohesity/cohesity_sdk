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
    AAGInfo
    ArchivalTargetSummaryInfo
    CommonRecoverObjectSnapshotParams
    CommonRecoverSqlAppTargetParams
    HostInformation
    MssqlObjectEntityParams
    ObjectSummary
    RecoverSqlAppParamsAllOf


class RecoverSqlAppParams(ModelComposed):
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
        ('target_environment',): {
            'KSQL': "kSQL",
        },
        ('snapshot_target_type',): {
            'None': None,
            'LOCAL': "Local",
            'ARCHIVAL': "Archival",
            'RPAASARCHIVAL': "RpaasArchival",
            'STORAGEARRAYSNAPSHOT': "StorageArraySnapshot",
            'REMOTE': "Remote",
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
            'FINALIZING': "Finalizing",
            'SKIPPED': "Skipped",
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
            'snapshot_id': (str,),  # noqa: E501
            'target_environment': (str,),  # noqa: E501
            'archival_target_info': (ArchivalTargetSummaryInfo,),  # noqa: E501
            'bytes_restored': (int,),  # noqa: E501
            'end_time_usecs': (int,),  # noqa: E501
            'messages': (list[str],),  # noqa: E501
            'object_info': (ObjectSummary,),  # noqa: E501
            'point_in_time_usecs': (int,),  # noqa: E501
            'progress_task_id': (str,),  # noqa: E501
            'protection_group_id': (str,),  # noqa: E501
            'protection_group_name': (str,),  # noqa: E501
            'recover_from_standby': (bool,),  # noqa: E501
            'snapshot_creation_time_usecs': (int,),  # noqa: E501
            'snapshot_target_type': (str,),  # noqa: E501
            'start_time_usecs': (int,),  # noqa: E501
            'status': (str,),  # noqa: E501
            'storage_domain_id': (int,),  # noqa: E501
            'aag_info': (AAGInfo,),  # noqa: E501
            'host_info': (HostInformation,),  # noqa: E501
            'is_encrypted': (bool,),  # noqa: E501
            'sql_target_params': (CommonRecoverSqlAppTargetParams,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None



    attribute_map = {
        'snapshot_id': 'snapshotId',  # noqa: E501
        'target_environment': 'targetEnvironment',  # noqa: E501
        'archival_target_info': 'archivalTargetInfo',  # noqa: E501
        'bytes_restored': 'bytesRestored',  # noqa: E501
        'end_time_usecs': 'endTimeUsecs',  # noqa: E501
        'messages': 'messages',  # noqa: E501
        'object_info': 'objectInfo',  # noqa: E501
        'point_in_time_usecs': 'pointInTimeUsecs',  # noqa: E501
        'progress_task_id': 'progressTaskId',  # noqa: E501
        'protection_group_id': 'protectionGroupId',  # noqa: E501
        'protection_group_name': 'protectionGroupName',  # noqa: E501
        'recover_from_standby': 'recoverFromStandby',  # noqa: E501
        'snapshot_creation_time_usecs': 'snapshotCreationTimeUsecs',  # noqa: E501
        'snapshot_target_type': 'snapshotTargetType',  # noqa: E501
        'start_time_usecs': 'startTimeUsecs',  # noqa: E501
        'status': 'status',  # noqa: E501
        'storage_domain_id': 'storageDomainId',  # noqa: E501
        'aag_info': 'aagInfo',  # noqa: E501
        'host_info': 'hostInfo',  # noqa: E501
        'is_encrypted': 'isEncrypted',  # noqa: E501
        'sql_target_params': 'sqlTargetParams',  # noqa: E501
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
    def __init__(self, snapshot_id, target_environment, *args, **kwargs):  # noqa: E501
        """RecoverSqlAppParams - a model defined in OpenAPI

        Args:
            snapshot_id (str): Specifies the snapshot id.
            target_environment (str): Specifies the environment of the recovery target. The corresponding params below must be filled out.

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

            archival_target_info (ArchivalTargetSummaryInfo): [optional]  # noqa: E501
            bytes_restored (int): Specify the total bytes restored.. [optional]  # noqa: E501
            end_time_usecs (int): Specifies the end time of the Recovery in Unix timestamp epoch in microseconds. This field will be populated only after Recovery is finished.. [optional]  # noqa: E501
            messages (list[str]): Specify error messages about the object.. [optional]  # noqa: E501
            object_info (ObjectSummary): [optional]  # noqa: E501
            point_in_time_usecs (int): Specifies the timestamp (in microseconds. from epoch) for recovering to a point-in-time in the past.. [optional]  # noqa: E501
            progress_task_id (str): Progress monitor task id for Recovery of VM.. [optional]  # noqa: E501
            protection_group_id (str): Specifies the protection group id of the object snapshot.. [optional]  # noqa: E501
            protection_group_name (str): Specifies the protection group name of the object snapshot.. [optional]  # noqa: E501
            recover_from_standby (bool): Specifies that user wants to perform standby restore if it is enabled for this object.. [optional]  # noqa: E501
            snapshot_creation_time_usecs (int): Specifies the time when the snapshot is created in Unix timestamp epoch in microseconds.. [optional]  # noqa: E501
            snapshot_target_type (str): Specifies the snapshot target type.. [optional]  # noqa: E501
            start_time_usecs (int): Specifies the start time of the Recovery in Unix timestamp epoch in microseconds.. [optional]  # noqa: E501
            status (str): Status of the Recovery. 'Running' indicates that the Recovery is still running. 'Canceled' indicates that the Recovery has been cancelled. 'Canceling' indicates that the Recovery is in the process of being cancelled. 'Failed' indicates that the Recovery has failed. 'Succeeded' indicates that the Recovery has finished successfully. 'SucceededWithWarning' indicates that the Recovery finished successfully, but there were some warning messages. 'Skipped' indicates that the Recovery task was skipped.. [optional]  # noqa: E501
            storage_domain_id (int): Specifies the ID of the Storage Domain where this snapshot is stored.. [optional]  # noqa: E501
            aag_info (AAGInfo): [optional]  # noqa: E501
            host_info (HostInformation): [optional]  # noqa: E501
            is_encrypted (bool): Specifies whether the database is TDE enabled.. [optional]  # noqa: E501
            sql_target_params (CommonRecoverSqlAppTargetParams): [optional]  # noqa: E501
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
            'snapshot_id': snapshot_id,
            'target_environment': target_environment,
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
              CommonRecoverObjectSnapshotParams,
              MssqlObjectEntityParams,
              RecoverSqlAppParamsAllOf,
          ],
          'oneOf': [
          ],
        }

