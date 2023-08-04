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
    from cohesity_sdk.cluster.model.common_protection_group_request_paramsdc3738211b78497f_a31b107b557906d5_hdfs_protection_group_params_wrapper_all_of import CommonProtectionGroupRequestParamsdc3738211b78497fA31b107b557906d5HdfsProtectionGroupParamsWrapperAllOf
    from cohesity_sdk.cluster.model.common_protection_group_response_params1adf5af12d9e4081_a117_de198444a79b import CommonProtectionGroupResponseParams1adf5af12d9e4081A117De198444a79b
    from cohesity_sdk.cluster.model.hdfs_protection_group_params import HdfsProtectionGroupParams
    from cohesity_sdk.cluster.model.missing_entity_params import MissingEntityParams
    from cohesity_sdk.cluster.model.protection_group_alerting_policy import ProtectionGroupAlertingPolicy
    from cohesity_sdk.cluster.model.protection_group_run import ProtectionGroupRun
    from cohesity_sdk.cluster.model.sla_rule import SlaRule
    from cohesity_sdk.cluster.model.tenant import Tenant
    from cohesity_sdk.cluster.model.time_of_day import TimeOfDay
    globals()['CommonProtectionGroupRequestParamsdc3738211b78497fA31b107b557906d5HdfsProtectionGroupParamsWrapperAllOf'] = CommonProtectionGroupRequestParamsdc3738211b78497fA31b107b557906d5HdfsProtectionGroupParamsWrapperAllOf
    globals()['CommonProtectionGroupResponseParams1adf5af12d9e4081A117De198444a79b'] = CommonProtectionGroupResponseParams1adf5af12d9e4081A117De198444a79b
    globals()['HdfsProtectionGroupParams'] = HdfsProtectionGroupParams
    globals()['MissingEntityParams'] = MissingEntityParams
    globals()['ProtectionGroupAlertingPolicy'] = ProtectionGroupAlertingPolicy
    globals()['ProtectionGroupRun'] = ProtectionGroupRun
    globals()['SlaRule'] = SlaRule
    globals()['Tenant'] = Tenant
    globals()['TimeOfDay'] = TimeOfDay


class CommonProtectionGroupResponseParams1adf5af12d9e4081A117De198444a79bHdfsProtectionGroupParamsWrapper(ModelComposed):
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
        ('priority',): {
            'None': None,
            'KLOW': "kLow",
            'KMEDIUM': "kMedium",
            'KHIGH': "kHigh",
        },
        ('qos_policy',): {
            'None': None,
            'KBACKUPHDD': "kBackupHDD",
            'KBACKUPSSD': "kBackupSSD",
            'KTESTANDDEVHIGH': "kTestAndDevHigh",
            'KBACKUPALL': "kBackupAll",
        },
        ('environment',): {
            'None': None,
            'KVMWARE': "kVMware",
            'KHYPERV': "kHyperV",
            'KVCD': "kVCD",
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
        lazy_import()
        return {
            'id': (str, none_type,),  # noqa: E501
            'name': (str, none_type,),  # noqa: E501
            'cluster_id': (str, none_type,),  # noqa: E501
            'region_id': (str, none_type,),  # noqa: E501
            'policy_id': (str, none_type,),  # noqa: E501
            'priority': (str, none_type,),  # noqa: E501
            'storage_domain_id': (int, none_type,),  # noqa: E501
            'description': (str, none_type,),  # noqa: E501
            'start_time': (TimeOfDay,),  # noqa: E501
            'end_time_usecs': (int, none_type,),  # noqa: E501
            'alert_policy': (ProtectionGroupAlertingPolicy,),  # noqa: E501
            'sla': ([SlaRule], none_type,),  # noqa: E501
            'qos_policy': (str, none_type,),  # noqa: E501
            'abort_in_blackouts': (bool, none_type,),  # noqa: E501
            'pause_in_blackouts': (bool, none_type,),  # noqa: E501
            'is_active': (bool, none_type,),  # noqa: E501
            'is_deleted': (bool, none_type,),  # noqa: E501
            'is_paused': (bool, none_type,),  # noqa: E501
            'environment': (str, none_type,),  # noqa: E501
            'last_run': (ProtectionGroupRun,),  # noqa: E501
            'permissions': ([Tenant], none_type,),  # noqa: E501
            'is_protect_once': (bool, none_type,),  # noqa: E501
            'missing_entities': ([MissingEntityParams], none_type,),  # noqa: E501
            'num_protected_objects': (int, none_type,),  # noqa: E501
            'hdfs_params': (HdfsProtectionGroupParams,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None



    attribute_map = {
        'id': 'id',  # noqa: E501
        'name': 'name',  # noqa: E501
        'cluster_id': 'clusterId',  # noqa: E501
        'region_id': 'regionId',  # noqa: E501
        'policy_id': 'policyId',  # noqa: E501
        'priority': 'priority',  # noqa: E501
        'storage_domain_id': 'storageDomainId',  # noqa: E501
        'description': 'description',  # noqa: E501
        'start_time': 'startTime',  # noqa: E501
        'end_time_usecs': 'endTimeUsecs',  # noqa: E501
        'alert_policy': 'alertPolicy',  # noqa: E501
        'sla': 'sla',  # noqa: E501
        'qos_policy': 'qosPolicy',  # noqa: E501
        'abort_in_blackouts': 'abortInBlackouts',  # noqa: E501
        'pause_in_blackouts': 'pauseInBlackouts',  # noqa: E501
        'is_active': 'isActive',  # noqa: E501
        'is_deleted': 'isDeleted',  # noqa: E501
        'is_paused': 'isPaused',  # noqa: E501
        'environment': 'environment',  # noqa: E501
        'last_run': 'lastRun',  # noqa: E501
        'permissions': 'permissions',  # noqa: E501
        'is_protect_once': 'isProtectOnce',  # noqa: E501
        'missing_entities': 'missingEntities',  # noqa: E501
        'num_protected_objects': 'numProtectedObjects',  # noqa: E501
        'hdfs_params': 'hdfsParams',  # noqa: E501
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
        """CommonProtectionGroupResponseParams1adf5af12d9e4081A117De198444a79bHdfsProtectionGroupParamsWrapper - a model defined in OpenAPI

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

            id (str, none_type): Specifies the ID of the Protection Group.. [optional]  # noqa: E501
            name (str, none_type): Specifies the name of the Protection Group.. [optional]  # noqa: E501
            cluster_id (str, none_type): Specifies the cluster ID.. [optional]  # noqa: E501
            region_id (str, none_type): Specifies the region ID.. [optional]  # noqa: E501
            policy_id (str, none_type): Specifies the unique id of the Protection Policy associated with the Protection Group. The Policy provides retry settings Protection Schedules, Priority, SLA, etc.. [optional]  # noqa: E501
            priority (str, none_type): Specifies the priority of the Protection Group.. [optional]  # noqa: E501
            storage_domain_id (int, none_type): Specifies the Storage Domain (View Box) ID where this Protection Group writes data.. [optional]  # noqa: E501
            description (str, none_type): Specifies a description of the Protection Group.. [optional]  # noqa: E501
            start_time (TimeOfDay): [optional]  # noqa: E501
            end_time_usecs (int, none_type): Specifies the end time in micro seconds for this Protection Group. If this is not specified, the Protection Group won't be ended.. [optional]  # noqa: E501
            alert_policy (ProtectionGroupAlertingPolicy): [optional]  # noqa: E501
            sla ([SlaRule], none_type): Specifies the SLA parameters for this Protection Group.. [optional]  # noqa: E501
            qos_policy (str, none_type): Specifies whether the Protection Group will be written to HDD or SSD.. [optional]  # noqa: E501
            abort_in_blackouts (bool, none_type): Specifies whether currently executing jobs should abort if a blackout period specified by a policy starts. Available only if the selected policy has at least one blackout period. Default value is false.. [optional]  # noqa: E501
            pause_in_blackouts (bool, none_type): Specifies whether currently executing jobs should be paused if a blackout period specified by a policy starts. Available only if the selected policy has at least one blackout period. Default value is false. This field should not be set to true if 'abortInBlackouts' is sent as true.. [optional]  # noqa: E501
            is_active (bool, none_type): Specifies if the Protection Group is active or not.. [optional]  # noqa: E501
            is_deleted (bool, none_type): Specifies if the Protection Group has been deleted.. [optional]  # noqa: E501
            is_paused (bool, none_type): Specifies if the the Protection Group is paused. New runs are not scheduled for the paused Protection Groups. Active run if any is not impacted.. [optional]  # noqa: E501
            environment (str, none_type): Specifies the environment of the Protection Group.. [optional]  # noqa: E501
            last_run (ProtectionGroupRun): [optional]  # noqa: E501
            permissions ([Tenant], none_type): Specifies the list of tenants that have permissions for this protection group.. [optional]  # noqa: E501
            is_protect_once (bool, none_type): Specifies if the the Protection Group is using a protect once type of policy. This field is helpful to identify run happen for this group.. [optional]  # noqa: E501
            missing_entities ([MissingEntityParams], none_type): Specifies the Information about missing entities.. [optional]  # noqa: E501
            num_protected_objects (int, none_type): Specifies the number of protected objects of the Protection Group.. [optional]  # noqa: E501
            hdfs_params (HdfsProtectionGroupParams): [optional]  # noqa: E501
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
              CommonProtectionGroupRequestParamsdc3738211b78497fA31b107b557906d5HdfsProtectionGroupParamsWrapperAllOf,
              CommonProtectionGroupResponseParams1adf5af12d9e4081A117De198444a79b,
          ],
          'oneOf': [
          ],
        }

