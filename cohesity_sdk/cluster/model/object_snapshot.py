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


class ObjectSnapshot(ModelNormal):
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
        ('snapshot_target_type',): {
            'None': None,
            'LOCAL': "Local",
            'ARCHIVAL': "Archival",
            'RPAASARCHIVAL': "RpaasArchival",
            'STORAGEARRAYSNAPSHOT': "StorageArraySnapshot",
        },
        ('indexing_status',): {
            'None': None,
            'INPROGRESS': "InProgress",
            'DONE': "Done",
            'NOINDEX': "NoIndex",
            'ERROR': "Error",
        },
        ('run_type',): {
            'None': None,
            'KREGULAR': "kRegular",
            'KFULL': "kFull",
            'KLOG': "kLog",
            'KSYSTEM': "kSystem",
            'KHYDRATECDP': "kHydrateCDP",
            'KSTORAGEARRAYSNAPSHOT': "kStorageArraySnapshot",
        },
        ('environment',): {
            'None': None,
            'KVMWARE': "kVMware",
            'KHYPERV': "kHyperV",
            'KAZURE': "kAzure",
            'KKVM': "kKVM",
            'KAWS': "kAWS",
            'KACROPOLIS': "kAcropolis",
            'KGCP': "kGCP",
            'KPHYSICAL': "kPhysical",
            'KPHYSICALFILES': "kPhysicalFiles",
            'KISILON': "kIsilon",
            'KNETAPP': "kNetapp",
            'KGENERICNAS': "kGenericNas",
            'KFLASHBLADE': "kFlashBlade",
            'KELASTIFILE': "kElastifile",
            'KGPFS': "kGPFS",
            'KPURE': "kPure",
            'KNIMBLE': "kNimble",
            'KSQL': "kSQL",
            'KORACLE': "kOracle",
            'KEXCHANGE': "kExchange",
            'KAD': "kAD",
            'KVIEW': "kView",
            'KO365': "kO365",
            'KHYPERFLEX': "kHyperFlex",
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
        ('protection_group_id',): {
            'regex': {
                'pattern': r'^\d+:\d+:\d+$',  # noqa: E501
            },
        },

        ('protection_group_run_id',): {
            'regex': {
                'pattern': r'^\d+:\d+$',  # noqa: E501
            },
        },

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
            'id': (str, none_type,),  # noqa: E501
            'snapshot_target_type': (str, none_type,),  # noqa: E501
            'indexing_status': (str, none_type,),  # noqa: E501
            'protection_group_id': (str, none_type,),  # noqa: E501
            'protection_group_name': (str, none_type,),  # noqa: E501
            'protection_group_run_id': (str, none_type,),  # noqa: E501
            'run_instance_id': (int, none_type,),  # noqa: E501
            'run_start_time_usecs': (int, none_type,),  # noqa: E501
            'source_group_id': (str, none_type,),  # noqa: E501
            'run_type': (str, none_type,),  # noqa: E501
            'environment': (str, none_type,),  # noqa: E501
            'snapshot_timestamp_usecs': (int, none_type,),  # noqa: E501
            'expiry_time_usecs': (int, none_type,),  # noqa: E501
            'external_target_info': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type,),  # noqa: E501
            'storage_domain_id': (int, none_type,),  # noqa: E501
            'has_data_lock': (bool, none_type,),  # noqa: E501
            'on_legal_hold': (bool, none_type,),  # noqa: E501
            'object_id': (int, none_type,),  # noqa: E501
            'object_name': (str, none_type,),  # noqa: E501
            'source_id': (int, none_type,),  # noqa: E501
            'region_id': (str, none_type,),  # noqa: E501
            'cluster_id': (int, none_type,),  # noqa: E501
            'cluster_incarnation_id': (int, none_type,),  # noqa: E501
            'physical_params': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'hyperv_params': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'aws_params': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'azure_params': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'netapp_params': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'isilon_params': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'gpfs_params': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'flashblade_params': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'generic_nas_params': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'elastifile_params': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'sfdc_params': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None



    attribute_map = {
        'id': 'id',  # noqa: E501
        'snapshot_target_type': 'snapshotTargetType',  # noqa: E501
        'indexing_status': 'indexingStatus',  # noqa: E501
        'protection_group_id': 'protectionGroupId',  # noqa: E501
        'protection_group_name': 'protectionGroupName',  # noqa: E501
        'protection_group_run_id': 'protectionGroupRunId',  # noqa: E501
        'run_instance_id': 'runInstanceId',  # noqa: E501
        'run_start_time_usecs': 'runStartTimeUsecs',  # noqa: E501
        'source_group_id': 'sourceGroupId',  # noqa: E501
        'run_type': 'runType',  # noqa: E501
        'environment': 'environment',  # noqa: E501
        'snapshot_timestamp_usecs': 'snapshotTimestampUsecs',  # noqa: E501
        'expiry_time_usecs': 'expiryTimeUsecs',  # noqa: E501
        'external_target_info': 'externalTargetInfo',  # noqa: E501
        'storage_domain_id': 'storageDomainId',  # noqa: E501
        'has_data_lock': 'hasDataLock',  # noqa: E501
        'on_legal_hold': 'onLegalHold',  # noqa: E501
        'object_id': 'objectId',  # noqa: E501
        'object_name': 'objectName',  # noqa: E501
        'source_id': 'sourceId',  # noqa: E501
        'region_id': 'regionId',  # noqa: E501
        'cluster_id': 'clusterId',  # noqa: E501
        'cluster_incarnation_id': 'clusterIncarnationId',  # noqa: E501
        'physical_params': 'physicalParams',  # noqa: E501
        'hyperv_params': 'hypervParams',  # noqa: E501
        'aws_params': 'awsParams',  # noqa: E501
        'azure_params': 'azureParams',  # noqa: E501
        'netapp_params': 'netappParams',  # noqa: E501
        'isilon_params': 'isilonParams',  # noqa: E501
        'gpfs_params': 'gpfsParams',  # noqa: E501
        'flashblade_params': 'flashbladeParams',  # noqa: E501
        'generic_nas_params': 'genericNasParams',  # noqa: E501
        'elastifile_params': 'elastifileParams',  # noqa: E501
        'sfdc_params': 'sfdcParams',  # noqa: E501
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
        """ObjectSnapshot - a model defined in OpenAPI

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

            id (str, none_type): Specifies the id of the snapshot.. [optional]  # noqa: E501
            snapshot_target_type (str, none_type): Specifies the target type where the Object's snapshot resides.. [optional]  # noqa: E501
            indexing_status (str, none_type): Specifies the indexing status of objects in this snapshot.<br> 'InProgress' indicates the indexing is in progress.<br> 'Done' indicates indexing is done.<br> 'NoIndex' indicates indexing is not applicable.<br> 'Error' indicates indexing failed with error.. [optional]  # noqa: E501
            protection_group_id (str, none_type): Specifies id of the Protection Group.. [optional]  # noqa: E501
            protection_group_name (str, none_type): Specifies name of the Protection Group.. [optional]  # noqa: E501
            protection_group_run_id (str, none_type): Specifies id of the Protection Group Run.. [optional]  # noqa: E501
            run_instance_id (int, none_type): Specifies the instance id of the protection run which create the snapshot.. [optional]  # noqa: E501
            run_start_time_usecs (int, none_type): Specifies the start time of the run in micro seconds.. [optional]  # noqa: E501
            source_group_id (str, none_type): Specifies the source protection group id in case of replication.. [optional]  # noqa: E501
            run_type (str, none_type): Specifies the type of protection run created this snapshot.. [optional]  # noqa: E501
            environment (str, none_type): Specifies the snapshot environment.. [optional]  # noqa: E501
            snapshot_timestamp_usecs (int, none_type): Specifies the timestamp in Unix time epoch in microseconds when the snapshot is taken for the specified Object.. [optional]  # noqa: E501
            expiry_time_usecs (int, none_type): Specifies the expiry time of the snapshot in Unix timestamp epoch in microseconds. If the snapshot has no expiry, this property will not be set.. [optional]  # noqa: E501
            external_target_info ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type): Specifies the external target information if this is an archival snapshot.. [optional]  # noqa: E501
            storage_domain_id (int, none_type): Specifies the Storage Domain id where the snapshot of object is present.. [optional]  # noqa: E501
            has_data_lock (bool, none_type): Specifies if this snapshot has datalock.. [optional]  # noqa: E501
            on_legal_hold (bool, none_type): Specifies if this snapshot is on legalhold.. [optional]  # noqa: E501
            object_id (int, none_type): Specifies the object id which the snapshot is taken from.. [optional]  # noqa: E501
            object_name (str, none_type): Specifies the object name which the snapshot is taken from.. [optional]  # noqa: E501
            source_id (int, none_type): Specifies the object source id which the snapshot is taken from.. [optional]  # noqa: E501
            region_id (str, none_type): Specifies the region id where this snapshot belongs to.. [optional]  # noqa: E501
            cluster_id (int, none_type): Specifies the cluster id where this snapshot belongs to.. [optional]  # noqa: E501
            cluster_incarnation_id (int, none_type): Specifies the cluster incarnation id where this snapshot belongs to.. [optional]  # noqa: E501
            physical_params ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Specifies the parameters specific to Physical type snapshot.. [optional]  # noqa: E501
            hyperv_params ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Specifies the parameters specific to HyperV type snapshot.. [optional]  # noqa: E501
            aws_params ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Specifies the parameters specific to AWS type snapshot.. [optional]  # noqa: E501
            azure_params ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Specifies the parameters specific to Azure type snapshot.. [optional]  # noqa: E501
            netapp_params ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Specifies the parameters specific to NetApp type snapshot.. [optional]  # noqa: E501
            isilon_params ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Specifies the parameters specific to Isilon type snapshot.. [optional]  # noqa: E501
            gpfs_params ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Specifies the parameters specific to GPFS type snapshot.. [optional]  # noqa: E501
            flashblade_params ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Specifies the parameters specific to Flashblade type snapshot.. [optional]  # noqa: E501
            generic_nas_params ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Specifies the parameters specific to Generic NAS type snapshot.. [optional]  # noqa: E501
            elastifile_params ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Specifies the parameters specific to NetApp type snapshot.. [optional]  # noqa: E501
            sfdc_params ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Specifies the parameters specific to Salesforce type snapshot.. [optional]  # noqa: E501
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

