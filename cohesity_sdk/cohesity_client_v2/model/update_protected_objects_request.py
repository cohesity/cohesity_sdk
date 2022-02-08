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
    from cohesity_sdk.cohesity_client_v2.model.common_object_protect_params import CommonObjectProtectParams
    from cohesity_sdk.cohesity_client_v2.model.elastifile_object_protection_update_request_params import ElastifileObjectProtectionUpdateRequestParams
    from cohesity_sdk.cohesity_client_v2.model.env_specific_object_protection_update_request_params import EnvSpecificObjectProtectionUpdateRequestParams
    from cohesity_sdk.cohesity_client_v2.model.flashblade_object_protection_update_request_params import FlashbladeObjectProtectionUpdateRequestParams
    from cohesity_sdk.cohesity_client_v2.model.generic_nas_object_protection_update_request_params import GenericNasObjectProtectionUpdateRequestParams
    from cohesity_sdk.cohesity_client_v2.model.gpfs_object_protection_update_request_params import GpfsObjectProtectionUpdateRequestParams
    from cohesity_sdk.cohesity_client_v2.model.isilon_object_protection_update_request_params import IsilonObjectProtectionUpdateRequestParams
    from cohesity_sdk.cohesity_client_v2.model.mssql_object_protection_update_request_params import MssqlObjectProtectionUpdateRequestParams
    from cohesity_sdk.cohesity_client_v2.model.netapp_object_protection_update_request_params import NetappObjectProtectionUpdateRequestParams
    from cohesity_sdk.cohesity_client_v2.model.office365_user_mailbox_object_protection_update_request_params import Office365UserMailboxObjectProtectionUpdateRequestParams
    from cohesity_sdk.cohesity_client_v2.model.sla_rule import SlaRule
    from cohesity_sdk.cohesity_client_v2.model.time_of_day import TimeOfDay
    from cohesity_sdk.cohesity_client_v2.model.vmware_object_protection_update_request_params import VmwareObjectProtectionUpdateRequestParams
    globals()['CommonObjectProtectParams'] = CommonObjectProtectParams
    globals()['ElastifileObjectProtectionUpdateRequestParams'] = ElastifileObjectProtectionUpdateRequestParams
    globals()['EnvSpecificObjectProtectionUpdateRequestParams'] = EnvSpecificObjectProtectionUpdateRequestParams
    globals()['FlashbladeObjectProtectionUpdateRequestParams'] = FlashbladeObjectProtectionUpdateRequestParams
    globals()['GenericNasObjectProtectionUpdateRequestParams'] = GenericNasObjectProtectionUpdateRequestParams
    globals()['GpfsObjectProtectionUpdateRequestParams'] = GpfsObjectProtectionUpdateRequestParams
    globals()['IsilonObjectProtectionUpdateRequestParams'] = IsilonObjectProtectionUpdateRequestParams
    globals()['MssqlObjectProtectionUpdateRequestParams'] = MssqlObjectProtectionUpdateRequestParams
    globals()['NetappObjectProtectionUpdateRequestParams'] = NetappObjectProtectionUpdateRequestParams
    globals()['Office365UserMailboxObjectProtectionUpdateRequestParams'] = Office365UserMailboxObjectProtectionUpdateRequestParams
    globals()['SlaRule'] = SlaRule
    globals()['TimeOfDay'] = TimeOfDay
    globals()['VmwareObjectProtectionUpdateRequestParams'] = VmwareObjectProtectionUpdateRequestParams


class UpdateProtectedObjectsRequest(ModelComposed):
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
            'KAZURE': "kAzure",
            'KGCP': "kGCP",
            'KKVM': "kKVM",
            'KACROPOLIS': "kAcropolis",
            'KAWS': "kAWS",
            'KPHYSICAL': "kPhysical",
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
            'KKUBERNETES': "kKubernetes",
            'KCASSANDRA': "kCassandra",
            'KMONGODB': "kMongoDB",
            'KCOUCHBASE': "kCouchbase",
            'KHDFS': "kHdfs",
            'KHIVE': "kHive",
            'KHBASE': "kHBase",
            'KUDA': "kUDA",
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
            'policy_id': (str, none_type,),  # noqa: E501
            'storage_domain_id': (int, none_type,),  # noqa: E501
            'start_time': (TimeOfDay,),  # noqa: E501
            'priority': (str, none_type,),  # noqa: E501
            'sla': ([SlaRule], none_type,),  # noqa: E501
            'qos_policy': (str, none_type,),  # noqa: E501
            'abort_in_blackouts': (bool, none_type,),  # noqa: E501
            'environment': (str, none_type,),  # noqa: E501
            'vmware_params': (VmwareObjectProtectionUpdateRequestParams,),  # noqa: E501
            'generic_nas_params': (GenericNasObjectProtectionUpdateRequestParams,),  # noqa: E501
            'gpfs_params': (GpfsObjectProtectionUpdateRequestParams,),  # noqa: E501
            'elastifile_params': (ElastifileObjectProtectionUpdateRequestParams,),  # noqa: E501
            'netapp_params': (NetappObjectProtectionUpdateRequestParams,),  # noqa: E501
            'isilon_params': (IsilonObjectProtectionUpdateRequestParams,),  # noqa: E501
            'flashblade_params': (FlashbladeObjectProtectionUpdateRequestParams,),  # noqa: E501
            'mssql_params': (MssqlObjectProtectionUpdateRequestParams,),  # noqa: E501
            'office365_user_mailbox_params': (Office365UserMailboxObjectProtectionUpdateRequestParams,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None



    attribute_map = {
        'policy_id': 'policyId',  # noqa: E501
        'storage_domain_id': 'storageDomainId',  # noqa: E501
        'start_time': 'startTime',  # noqa: E501
        'priority': 'priority',  # noqa: E501
        'sla': 'sla',  # noqa: E501
        'qos_policy': 'qosPolicy',  # noqa: E501
        'abort_in_blackouts': 'abortInBlackouts',  # noqa: E501
        'environment': 'environment',  # noqa: E501
        'vmware_params': 'vmwareParams',  # noqa: E501
        'generic_nas_params': 'genericNasParams',  # noqa: E501
        'gpfs_params': 'gpfsParams',  # noqa: E501
        'elastifile_params': 'elastifileParams',  # noqa: E501
        'netapp_params': 'netappParams',  # noqa: E501
        'isilon_params': 'isilonParams',  # noqa: E501
        'flashblade_params': 'flashbladeParams',  # noqa: E501
        'mssql_params': 'mssqlParams',  # noqa: E501
        'office365_user_mailbox_params': 'office365UserMailboxParams',  # noqa: E501
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
    def __init__(self, policy_id, *args, **kwargs):  # noqa: E501
        """UpdateProtectedObjectsRequest - a model defined in OpenAPI

        Args:
            policy_id (str, none_type): Specifies the unique id of the Protection Policy. The Policy settings will be attached with every object and will be used in backup.

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

            storage_domain_id (int, none_type): Specifies the Storage Domain (View Box) ID where the object backup will be taken. This is not required if Cloud archive direct is benig used.. [optional]  # noqa: E501
            start_time (TimeOfDay): [optional]  # noqa: E501
            priority (str, none_type): Specifies the priority for the objects backup.. [optional]  # noqa: E501
            sla ([SlaRule], none_type): Specifies the SLA parameters for list of objects.. [optional]  # noqa: E501
            qos_policy (str, none_type): Specifies whether object backup will be written to HDD or SSD.. [optional]  # noqa: E501
            abort_in_blackouts (bool, none_type): Specifies whether currently executing object backup should abort if a blackout period specified by a policy starts. Available only if the selected policy has at least one blackout period. Default value is false.. [optional]  # noqa: E501
            environment (str, none_type): Specifies the environment for current object.. [optional]  # noqa: E501
            vmware_params (VmwareObjectProtectionUpdateRequestParams): [optional]  # noqa: E501
            generic_nas_params (GenericNasObjectProtectionUpdateRequestParams): [optional]  # noqa: E501
            gpfs_params (GpfsObjectProtectionUpdateRequestParams): [optional]  # noqa: E501
            elastifile_params (ElastifileObjectProtectionUpdateRequestParams): [optional]  # noqa: E501
            netapp_params (NetappObjectProtectionUpdateRequestParams): [optional]  # noqa: E501
            isilon_params (IsilonObjectProtectionUpdateRequestParams): [optional]  # noqa: E501
            flashblade_params (FlashbladeObjectProtectionUpdateRequestParams): [optional]  # noqa: E501
            mssql_params (MssqlObjectProtectionUpdateRequestParams): [optional]  # noqa: E501
            office365_user_mailbox_params (Office365UserMailboxObjectProtectionUpdateRequestParams): [optional]  # noqa: E501
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
            'policy_id': policy_id,
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
              CommonObjectProtectParams,
              EnvSpecificObjectProtectionUpdateRequestParams,
          ],
          'oneOf': [
          ],
        }

