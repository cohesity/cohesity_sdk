"""
    Cohesity REST API

    Cohesity API provides a RESTful interface to access the various data management operations on Cohesity cluster and Helios.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from cohesity_sdk.helios.model_utils import (  # noqa: F401
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


class McmObjectBackupRunActivityParams(ModelNormal):
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
            'FINALIZING': "Finalizing",
        },
        ('protection_environment_type',): {
            'None': None,
            'KVMWARE': "kVMware",
            'KHYPERV': "kHyperV",
            'KAZURE': "kAzure",
            'KGCP': "kGCP",
            'KKVM': "kKVM",
            'KACROPOLIS': "kAcropolis",
            'KAWS': "kAWS",
            'KAWSNATIVE': "kAWSNative",
            'KAWSSNAPSHOTMANAGER': "kAWSSnapshotManager",
            'KRDSSNAPSHOTMANAGER': "kRDSSnapshotManager",
            'KAURORASNAPSHOTMANAGER': "kAuroraSnapshotManager",
            'KPHYSICAL': "kPhysical",
            'KPHYSICALFILES': "kPhysicalFiles",
            'KGPFS': "kGPFS",
            'KELASTIFILE': "kElastifile",
            'KNETAPP': "kNetapp",
            'KGENERICNAS': "kGenericNas",
            'KISILON': "kIsilon",
            'KFLASHBLADE': "kFlashBlade",
            'KPURE': "kPure",
            'KSQL': "kSQL",
            'KEXCHANGE': "kExchange",
            'KAD': "kAD",
            'KORACLE': "kOracle",
            'KVIEW': "kView",
            'KREMOTEADAPTER': "kRemoteAdapter",
            'KO365': "kO365",
            'KO365PUBLICFOLDERS': "kO365PublicFolders",
            'KO365TEAMS': "kO365Teams",
            'KO365GROUP': "kO365Group",
            'KO365EXCHANGE': "kO365Exchange",
            'KO365ONEDRIVE': "kO365OneDrive",
            'KO365SHAREPOINT': "kO365Sharepoint",
            'KKUBERNETES': "kKubernetes",
            'KCASSANDRA': "kCassandra",
            'KMONGODB': "kMongoDB",
            'KCOUCHBASE': "kCouchbase",
            'KHDFS': "kHdfs",
            'KHIVE': "kHive",
            'KHBASE': "kHBase",
            'KUDA': "kUDA",
            'KSFDC': "kSfdc",
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
        return {
            'run_id': (str, none_type,),  # noqa: E501
            'protection_group_id': (str, none_type,),  # noqa: E501
            'protection_group_name': (str, none_type,),  # noqa: E501
            'policy_id': (str, none_type,),  # noqa: E501
            'policy_name': (str, none_type,),  # noqa: E501
            'snapshot_id': (str, none_type,),  # noqa: E501
            'start_time_usecs': (int, none_type,),  # noqa: E501
            'end_time_usecs': (int, none_type,),  # noqa: E501
            'status': (str, none_type,),  # noqa: E501
            'progress_task_id': (str, none_type,),  # noqa: E501
            'protection_environment_type': (str, none_type,),  # noqa: E501
            'is_stubbed_run': (bool, none_type,),  # noqa: E501
            'is_sla_violated': (bool, none_type,),  # noqa: E501
            'logical_size_bytes': (int, none_type,),  # noqa: E501
            'bytes_written': (int, none_type,),  # noqa: E501
            'bytes_read': (int, none_type,),  # noqa: E501
            'message_code': (str, none_type,),  # noqa: E501
            'message_guid': (str, none_type,),  # noqa: E501
            'error_message': (str, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None



    attribute_map = {
        'run_id': 'runId',  # noqa: E501
        'protection_group_id': 'protectionGroupId',  # noqa: E501
        'protection_group_name': 'protectionGroupName',  # noqa: E501
        'policy_id': 'policyId',  # noqa: E501
        'policy_name': 'policyName',  # noqa: E501
        'snapshot_id': 'snapshotId',  # noqa: E501
        'start_time_usecs': 'startTimeUsecs',  # noqa: E501
        'end_time_usecs': 'endTimeUsecs',  # noqa: E501
        'status': 'status',  # noqa: E501
        'progress_task_id': 'progressTaskId',  # noqa: E501
        'protection_environment_type': 'protectionEnvironmentType',  # noqa: E501
        'is_stubbed_run': 'isStubbedRun',  # noqa: E501
        'is_sla_violated': 'isSlaViolated',  # noqa: E501
        'logical_size_bytes': 'logicalSizeBytes',  # noqa: E501
        'bytes_written': 'bytesWritten',  # noqa: E501
        'bytes_read': 'bytesRead',  # noqa: E501
        'message_code': 'messageCode',  # noqa: E501
        'message_guid': 'messageGuid',  # noqa: E501
        'error_message': 'errorMessage',  # noqa: E501
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
        """McmObjectBackupRunActivityParams - a model defined in OpenAPI

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

            run_id (str, none_type): Specifies the ID of the Protection Run.. [optional]  # noqa: E501
            protection_group_id (str, none_type): Specifies the Protection Group Id.. [optional]  # noqa: E501
            protection_group_name (str, none_type): Specifies the Protection Group name.. [optional]  # noqa: E501
            policy_id (str, none_type): Specifies the Protection Policy Id.. [optional]  # noqa: E501
            policy_name (str, none_type): Specifies the Protection Policy Name.. [optional]  # noqa: E501
            snapshot_id (str, none_type): Specifies the id of the object snapshot that is created as a part of this Run. This field is only populated for runs which are successful.. [optional]  # noqa: E501
            start_time_usecs (int, none_type): Specifies the start time of Run in Unix epoch Timestamp(in microseconds).. [optional]  # noqa: E501
            end_time_usecs (int, none_type): Specifies the end time of Run in Unix epoch Timestamp(in microseconds).. [optional]  # noqa: E501
            status (str, none_type): Status of the Run. 'Running' indicates that the run is still running. 'Canceled' indicates that the run has been canceled. 'Canceling' indicates that the run is in the process of being canceled. 'Failed' indicates that the run has failed. 'Missed' indicates that the run was unable to take place at the scheduled time because the previous run was still happening. 'Succeeded' indicates that the run has finished successfully. 'SucceededWithWarning' indicates that the run finished successfully, but there were some warning messages.. [optional]  # noqa: E501
            progress_task_id (str, none_type): Progress monitor task id for the Run.. [optional]  # noqa: E501
            protection_environment_type (str, none_type): Specifies the type of protection environment.. [optional]  # noqa: E501
            is_stubbed_run (bool, none_type): Specifies whether this is a stubbed run. This is set by the server and if set to true, this run entry specifies the user intent to create a run instead of actual run itself. [optional]  # noqa: E501
            is_sla_violated (bool, none_type): Indicated if SLA has been violated for this run.. [optional]  # noqa: E501
            logical_size_bytes (int, none_type): Specifies total logical size of the object in bytes.. [optional]  # noqa: E501
            bytes_written (int, none_type): Specifies total size of data in bytes written after taking backup.. [optional]  # noqa: E501
            bytes_read (int, none_type): Specifies total logical bytes read for creating the snapshot.. [optional]  # noqa: E501
            message_code (str, none_type): Specifies a short message describing the type of error which occurred.. [optional]  # noqa: E501
            message_guid (str, none_type): Specifies the identifier of the error code.. [optional]  # noqa: E501
            error_message (str, none_type): Specifies the full text of the error message if any error occurs.. [optional]  # noqa: E501
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


