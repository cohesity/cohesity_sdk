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
    RecoveredOrClonedVmsRenameConfig
    RecoveryVlanConfig
    VmwareVmRecoveryTargetConfig


class VmwareTargetParamsForRecoverVM(ModelNormal):
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
        ('disk_provision_type',): {
            'None': None,
            'KTHICKLAZYZEROED': "kThickLazyZeroed",
            'KTHICKEAGERZERO': "kThickEagerZero",
            'KTHIN': "kThin",
            'KBACKEDUPDISKTYPE': "kBackedUpDiskType",
            'ORIGINALBACKUPDISK': "originalBackUpDisk",
        },
        ('recovery_process_type',): {
            'INSTANTRECOVERY': "InstantRecovery",
            'COPYRECOVERY': "CopyRecovery",
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
            'attempt_differential_restore': (bool,),  # noqa: E501
            'continue_on_error': (bool,),  # noqa: E501
            'disk_provision_type': (str,),  # noqa: E501
            'enable_nbdssl_fallback': (bool,),  # noqa: E501
            'is_multi_stage_restore': (bool,),  # noqa: E501
            'leverage_san_transport': (bool,),  # noqa: E501
            'overwrite_existing_vm': (bool,),  # noqa: E501
            'power_off_and_rename_existing_vm': (bool,),  # noqa: E501
            'power_on_vms': (bool,),  # noqa: E501
            'recovery_process_type': (str,),  # noqa: E501
            'recovery_target_config': (VmwareVmRecoveryTargetConfig,),  # noqa: E501
            'rename_recovered_vms_params': (RecoveredOrClonedVmsRenameConfig,),  # noqa: E501
            'vlan_config': (RecoveryVlanConfig,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None



    attribute_map = {
        'attempt_differential_restore': 'attemptDifferentialRestore',  # noqa: E501
        'continue_on_error': 'continueOnError',  # noqa: E501
        'disk_provision_type': 'diskProvisionType',  # noqa: E501
        'enable_nbdssl_fallback': 'enableNBDSSLFallback',  # noqa: E501
        'is_multi_stage_restore': 'isMultiStageRestore',  # noqa: E501
        'leverage_san_transport': 'leverageSanTransport',  # noqa: E501
        'overwrite_existing_vm': 'overwriteExistingVm',  # noqa: E501
        'power_off_and_rename_existing_vm': 'powerOffAndRenameExistingVm',  # noqa: E501
        'power_on_vms': 'powerOnVms',  # noqa: E501
        'recovery_process_type': 'recoveryProcessType',  # noqa: E501
        'recovery_target_config': 'recoveryTargetConfig',  # noqa: E501
        'rename_recovered_vms_params': 'renameRecoveredVmsParams',  # noqa: E501
        'vlan_config': 'vlanConfig',  # noqa: E501
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
        """VmwareTargetParamsForRecoverVM - a model defined in OpenAPI

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

            attempt_differential_restore (bool): Specifies whether to attempt differential restore.. [optional]  # noqa: E501
            continue_on_error (bool): Specifies whether to continue recovering other vms if one of vms failed to recover. Default value is false.. [optional]  # noqa: E501
            disk_provision_type (str): Specifies the Virtual Disk Provisioning Policies for Vmware VM. [optional]  # noqa: E501
            enable_nbdssl_fallback (bool): If this field is set to true and SAN transport recovery fails, then recovery will fallback to use NBDSSL transport. This field only applies if 'leverageSanTransport' is set to true.. [optional]  # noqa: E501
            is_multi_stage_restore (bool): Specifies whether this is a multistage restore which is used for migration/hot-standby purpose.. [optional]  # noqa: E501
            leverage_san_transport (bool): Specifies whether to enable SAN transport for copy recovery or not. [optional]  # noqa: E501
            overwrite_existing_vm (bool): Specifies whether to overwrite the VM at the target location. This is a data destructive operation and if this is selected, the original VM may no longer be accessible. This option is only applicable if renameRecoveredVmParams is null and powerOffAndRenameExistingVm is false. This option is not supported for vApp or vApp template recoveries. Default value is false.. [optional]  # noqa: E501
            power_off_and_rename_existing_vm (bool): Specifies whether to power off and mark the VM at the target location as deprecated. As an example, <vm_name> will be renamed to deprecated::<vm_name>, and a new VM with the name <vm_name> in place of the now deprecated VM. Both deprecated::<vm_name> and <vm_name> will exist on the primary, but the corresponding protection job will only backup <vm_name> on its next run. Only applicable if renameRecoveredVmParams is null and overwriteExistingVm is false. This option is not supported for vApp or vApp template recoveries. Default value is false.. [optional]  # noqa: E501
            power_on_vms (bool): Specifies whether to power on vms after recovery. If not specified, or false, recovered vms will be in powered off state.. [optional]  # noqa: E501
            recovery_process_type (str): Specifies type of Recovery Process to be used. InstantRecovery/CopyRecovery etc... Default value is InstantRecovery.. [optional]  # noqa: E501
            recovery_target_config (VmwareVmRecoveryTargetConfig): [optional]  # noqa: E501
            rename_recovered_vms_params (RecoveredOrClonedVmsRenameConfig): [optional]  # noqa: E501
            vlan_config (RecoveryVlanConfig): [optional]  # noqa: E501
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


