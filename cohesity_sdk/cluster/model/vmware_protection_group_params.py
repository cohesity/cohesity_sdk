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
    from cohesity_sdk.cluster.model.common_cdp_params import CommonCdpParams
    from cohesity_sdk.cluster.model.common_vmware_protection_params import (
        CommonVmwareProtectionParams,
    )
    from cohesity_sdk.cluster.model.disk_info import DiskInfo
    from cohesity_sdk.cluster.model.indexing_policy import IndexingPolicy
    from cohesity_sdk.cluster.model.pre_post_script_params import PrePostScriptParams
    from cohesity_sdk.cluster.model.vm_filter import VMFilter
    from cohesity_sdk.cluster.model.vmware_protection_group_extra_params import (
        VmwareProtectionGroupExtraParams,
    )
    from cohesity_sdk.cluster.model.vmware_protection_group_object_params import (
        VmwareProtectionGroupObjectParams,
    )
    from cohesity_sdk.cluster.model.vmware_protection_group_params_all_of import (
        VmwareProtectionGroupParamsAllOf,
    )
    from cohesity_sdk.cluster.model.vmware_protection_group_standby_resource_params import (
        VmwareProtectionGroupStandbyResourceParams,
    )

    globals()["CommonCdpParams"] = CommonCdpParams
    globals()["CommonVmwareProtectionParams"] = CommonVmwareProtectionParams
    globals()["DiskInfo"] = DiskInfo
    globals()["IndexingPolicy"] = IndexingPolicy
    globals()["PrePostScriptParams"] = PrePostScriptParams
    globals()["VMFilter"] = VMFilter
    globals()["VmwareProtectionGroupExtraParams"] = VmwareProtectionGroupExtraParams
    globals()["VmwareProtectionGroupObjectParams"] = VmwareProtectionGroupObjectParams
    globals()["VmwareProtectionGroupParamsAllOf"] = VmwareProtectionGroupParamsAllOf
    globals()[
        "VmwareProtectionGroupStandbyResourceParams"
    ] = VmwareProtectionGroupStandbyResourceParams


class VmwareProtectionGroupParams(ModelComposed):
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

    allowed_values = {}

    validations = {}

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
            "global_exclude_disks": (
                [DiskInfo],
                none_type,
            ),  # noqa: E501
            "objects": ([VmwareProtectionGroupObjectParams],),  # noqa: E501
            "standby_resource_objects": (
                [VmwareProtectionGroupStandbyResourceParams],
                none_type,
            ),  # noqa: E501
            "app_consistent_snapshot": (
                bool,
                none_type,
            ),  # noqa: E501
            "enable_nbdssl_fallback": (
                bool,
                none_type,
            ),  # noqa: E501
            "fallback_to_crash_consistent_snapshot": (
                bool,
                none_type,
            ),  # noqa: E501
            "indexing_policy": (IndexingPolicy,),  # noqa: E501
            "leverage_san_transport": (
                bool,
                none_type,
            ),  # noqa: E501
            "pre_post_script": (PrePostScriptParams,),  # noqa: E501
            "skip_physical_rdm_disks": (
                bool,
                none_type,
            ),  # noqa: E501
            "allow_parallel_runs": (
                bool,
                none_type,
            ),  # noqa: E501
            "cloud_migration": (
                bool,
                none_type,
            ),  # noqa: E501
            "exclude_filters": (
                [VMFilter],
                none_type,
            ),  # noqa: E501
            "exclude_object_ids": ([int, none_type],),  # noqa: E501
            "exclude_vm_tag_ids": ([[int]],),  # noqa: E501
            "leverage_hyperflex_snapshots": (
                bool,
                none_type,
            ),  # noqa: E501
            "leverage_nutanix_snapshots": (
                bool,
                none_type,
            ),  # noqa: E501
            "leverage_storage_snapshots": (
                bool,
                none_type,
            ),  # noqa: E501
            "source_id": (
                int,
                none_type,
            ),  # noqa: E501
            "source_name": (
                str,
                none_type,
            ),  # noqa: E501
            "vm_tag_ids": (
                [[int]],
                none_type,
            ),  # noqa: E501
            "enable_cdp_sync_replication": (
                bool,
                none_type,
            ),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None

    attribute_map = {
        "global_exclude_disks": "globalExcludeDisks",  # noqa: E501
        "objects": "objects",  # noqa: E501
        "standby_resource_objects": "standbyResourceObjects",  # noqa: E501
        "app_consistent_snapshot": "appConsistentSnapshot",  # noqa: E501
        "enable_nbdssl_fallback": "enableNBDSSLFallback",  # noqa: E501
        "fallback_to_crash_consistent_snapshot": "fallbackToCrashConsistentSnapshot",  # noqa: E501
        "indexing_policy": "indexingPolicy",  # noqa: E501
        "leverage_san_transport": "leverageSanTransport",  # noqa: E501
        "pre_post_script": "prePostScript",  # noqa: E501
        "skip_physical_rdm_disks": "skipPhysicalRDMDisks",  # noqa: E501
        "allow_parallel_runs": "allowParallelRuns",  # noqa: E501
        "cloud_migration": "cloudMigration",  # noqa: E501
        "exclude_filters": "excludeFilters",  # noqa: E501
        "exclude_object_ids": "excludeObjectIds",  # noqa: E501
        "exclude_vm_tag_ids": "excludeVmTagIds",  # noqa: E501
        "leverage_hyperflex_snapshots": "leverageHyperflexSnapshots",  # noqa: E501
        "leverage_nutanix_snapshots": "leverageNutanixSnapshots",  # noqa: E501
        "leverage_storage_snapshots": "leverageStorageSnapshots",  # noqa: E501
        "source_id": "sourceId",  # noqa: E501
        "source_name": "sourceName",  # noqa: E501
        "vm_tag_ids": "vmTagIds",  # noqa: E501
        "enable_cdp_sync_replication": "enableCdpSyncReplication",  # noqa: E501
    }

    required_properties = set(
        [
            "_data_store",
            "_check_type",
            "_spec_property_naming",
            "_path_to_item",
            "_configuration",
            "_visited_composed_classes",
            "_composed_instances",
            "_var_name_to_model_instances",
            "_additional_properties_model_instances",
        ]
    )

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """VmwareProtectionGroupParams - a model defined in OpenAPI

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

            global_exclude_disks ([DiskInfo], none_type): Specifies a list of disks to exclude from the backup.. [optional]  # noqa: E501
            objects ([VmwareProtectionGroupObjectParams]): Specifies the objects to include in the backup.. [optional]  # noqa: E501
            standby_resource_objects ([VmwareProtectionGroupStandbyResourceParams], none_type): Specifies the standby resource objects for this backup.. [optional]  # noqa: E501
            app_consistent_snapshot (bool, none_type): Specifies whether or not to quiesce apps and the file system in order to take app consistent snapshots.. [optional]  # noqa: E501
            enable_nbdssl_fallback (bool, none_type): If this field is set to true and SAN transport backup fails, then backup will fallback to use NBDSSL transport. This field only applies if 'leverageSanTransport' is set to true.. [optional]  # noqa: E501
            fallback_to_crash_consistent_snapshot (bool, none_type): Specifies whether or not to fallback to a crash consistent snapshot in the event that an app consistent snapshot fails. This parameter defaults to true and only changes the behavior of the operation if 'appConsistentSnapshot' is set to 'true'.. [optional]  # noqa: E501
            indexing_policy (IndexingPolicy): [optional]  # noqa: E501
            leverage_san_transport (bool, none_type): If this field is set to true, then the backup for the objects will be performed using dedicated storage area network (SAN) instead of LAN or managment network.. [optional]  # noqa: E501
            pre_post_script (PrePostScriptParams): [optional]  # noqa: E501
            skip_physical_rdm_disks (bool, none_type): Specifies whether or not to skip backing up physical RDM disks. Physical RDM disks cannot be backed up, so if you attempt to backup a VM with physical RDM disks and this value is set to 'false', then those VM backups will fail.. [optional]  # noqa: E501
            allow_parallel_runs (bool, none_type): Specifies whether or not this job can have parallel runs.. [optional]  # noqa: E501
            cloud_migration (bool, none_type): Specifies whether or not to move the workload to the cloud.. [optional]  # noqa: E501
            exclude_filters ([VMFilter], none_type): Specifies the list of exclusion filters applied during the group creation or edit. These exclusion filters can be wildcard supported strings or regular expressions. Objects satisfying these filters will be excluded during backup and also auto protected objects will be ignored if filtered by any of the filters.. [optional]  # noqa: E501
            exclude_object_ids ([int, none_type]): Specifies the list of IDs of the objects to not be protected in this backup. This field only applies if provided object id is non leaf entity such as Tag or a folder. This can be used to ignore specific objects under a parent object which has been included for protection.. [optional]  # noqa: E501
            exclude_vm_tag_ids ([[int]]): Array of Arrays of VM Tag Ids that Specify VMs to Exclude. Optionally specify a list of VMs to exclude from protecting by listing Protection Source ids of VM Tags in this two dimensional array. Using this two dimensional array of Tag ids, the Cluster generates a list of VMs to exclude from protecting, which are derived from intersections of the inner arrays and union of the outer array, as shown by the following example. For example a Datacenter is selected to be protected but you want to exclude all the 'Former Employees' VMs in the East and West but keep all the VMs for 'Former Employees' in the South which are also stored in this Datacenter, by specifying the following tag id array: [ [1000, 2221], [1000, 3031] ], where 1000 is the 'Former Employee' VM Tag id, 2221 is the 'East' VM Tag id and 3031 is the 'West' VM Tag id. The first inner array [1000, 2221] produces a list of VMs that are both tagged with 'Former Employees' and 'East' (an intersection). The second inner array [1000, 3031] produces a list of VMs that are both tagged with 'Former Employees' and 'West' (an intersection). The outer array combines the list of VMs from the two inner arrays. The list of resulting VMs are excluded from being protected this Job.. [optional]  # noqa: E501
            leverage_hyperflex_snapshots (bool, none_type): Whether to leverage the hyperflex based snapshots for this backup. To leverage hyperflex snapshots, it has to first be registered. If hyperflex based snapshots cannot be taken, backup will fallback to the default backup method.. [optional]  # noqa: E501
            leverage_nutanix_snapshots (bool, none_type): Whether to leverage the nutanix based snapshots for this backup. To leverage nutanix snapshots, it has to first be registered. If nutanix based snapshots cannot be taken, backup will fallback to the default backup method.. [optional]  # noqa: E501
            leverage_storage_snapshots (bool, none_type): Whether to leverage the storage array based snapshots for this backup. To leverage storage snapshots, the storage array has to be registered as a source. If storage based snapshots can not be taken, backup will fallback to the default backup method.. [optional]  # noqa: E501
            source_id (int, none_type): Specifies the id of the parent of the objects.. [optional]  # noqa: E501
            source_name (str, none_type): Specifies the name of the parent of the objects.. [optional]  # noqa: E501
            vm_tag_ids ([[int]], none_type): Array of Array of VM Tag Ids that Specify VMs to Protect. Optionally specify a list of VMs to protect by listing Protection Source ids of VM Tags in this two dimensional array. Using this two dimensional array of Tag ids, the Cluster generates a list of VMs to protect which are derived from intersections of the inner arrays and union of the outer array, as shown by the following example. To protect only 'Eng' VMs in the East and all the VMs in the West, specify the following tag id array: [ [1101, 2221], [3031] ], where 1101 is the 'Eng' VM Tag id, 2221 is the 'East' VM Tag id and 3031 is the 'West' VM Tag id. The inner array [1101, 2221] produces a list of VMs that are both tagged with 'Eng' and 'East' (an intersection). The outer array combines the list from the inner array with list of VMs tagged with 'West' (a union). The list of resulting VMs are protected by this Protection Group.. [optional]  # noqa: E501
            enable_cdp_sync_replication (bool, none_type): Specifies whether synchronous replication is enabled for CDP Protection Group when replication target is specified in attached policy.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop("_check_type", True)
        _spec_property_naming = kwargs.pop("_spec_property_naming", False)
        _path_to_item = kwargs.pop("_path_to_item", ())
        _configuration = kwargs.pop("_configuration", None)
        _visited_composed_classes = kwargs.pop("_visited_composed_classes", ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments."
                % (
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
            "_check_type": _check_type,
            "_path_to_item": _path_to_item,
            "_spec_property_naming": _spec_property_naming,
            "_configuration": _configuration,
            "_visited_composed_classes": self._visited_composed_classes,
        }
        required_args = {}
        model_args = {}
        model_args.update(required_args)
        model_args.update(kwargs)
        composed_info = validate_get_composed_info(constant_args, model_args, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        unused_args = composed_info[3]

        for var_name, var_value in required_args.items():
            setattr(self, var_name, var_value)
        for var_name, var_value in kwargs.items():
            if (
                var_name in unused_args
                and self._configuration is not None
                and self._configuration.discard_unknown_keys
                and not self._additional_properties_model_instances
            ):
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
            "anyOf": [],
            "allOf": [
                CommonCdpParams,
                CommonVmwareProtectionParams,
                VmwareProtectionGroupExtraParams,
                VmwareProtectionGroupParamsAllOf,
            ],
            "oneOf": [],
        }
