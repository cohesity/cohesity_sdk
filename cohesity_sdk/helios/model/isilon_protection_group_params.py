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


def lazy_import():
    from cohesity_sdk.helios.model.continuous_snapshot_params import (
        ContinuousSnapshotParams,
    )
    from cohesity_sdk.helios.model.file_filtering_policy import FileFilteringPolicy
    from cohesity_sdk.helios.model.file_level_data_lock_config import (
        FileLevelDataLockConfig,
    )
    from cohesity_sdk.helios.model.filter_ip_config import FilterIpConfig
    from cohesity_sdk.helios.model.host_based_backup_script_params import (
        HostBasedBackupScriptParams,
    )
    from cohesity_sdk.helios.model.indexing_policy import IndexingPolicy
    from cohesity_sdk.helios.model.isilon_protection_group_object_params import (
        IsilonProtectionGroupObjectParams,
    )
    from cohesity_sdk.helios.model.nas_throttling_config import NasThrottlingConfig

    globals()["ContinuousSnapshotParams"] = ContinuousSnapshotParams
    globals()["FileFilteringPolicy"] = FileFilteringPolicy
    globals()["FileLevelDataLockConfig"] = FileLevelDataLockConfig
    globals()["FilterIpConfig"] = FilterIpConfig
    globals()["HostBasedBackupScriptParams"] = HostBasedBackupScriptParams
    globals()["IndexingPolicy"] = IndexingPolicy
    globals()["IsilonProtectionGroupObjectParams"] = IsilonProtectionGroupObjectParams
    globals()["NasThrottlingConfig"] = NasThrottlingConfig


class IsilonProtectionGroupParams(ModelNormal):
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
        ("protocol",): {
            "None": None,
            "KNOPROTOCOL": "kNoProtocol",
            "KNFS3": "kNfs3",
            "KNFS4_1": "kNfs4_1",
            "KCIFS1": "kCifs1",
            "KCIFS2": "kCifs2",
            "KCIFS3": "kCifs3",
        },
    }

    validations = {
        ("objects",): {
            "min_items": 1,
        },
    }

    additional_properties_type = None

    _nullable = True

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
            "objects": ([IsilonProtectionGroupObjectParams],),  # noqa: E501
            "direct_cloud_archive": (
                bool,
                none_type,
            ),  # noqa: E501
            "native_format": (
                bool,
                none_type,
            ),  # noqa: E501
            "indexing_policy": (IndexingPolicy,),  # noqa: E501
            "protocol": (
                str,
                none_type,
            ),  # noqa: E501
            "continue_on_error": (
                bool,
                none_type,
            ),  # noqa: E501
            "encryption_enabled": (
                bool,
                none_type,
            ),  # noqa: E501
            "file_lock_config": (FileLevelDataLockConfig,),  # noqa: E501
            "file_filters": (FileFilteringPolicy,),  # noqa: E501
            "use_changelist": (
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
            "pre_post_script": (HostBasedBackupScriptParams,),  # noqa: E501
            "continuous_snapshots": (ContinuousSnapshotParams,),  # noqa: E501
            "filter_ip_config": (FilterIpConfig,),  # noqa: E501
            "throttling_config": (NasThrottlingConfig,),  # noqa: E501
            "modify_source_permissions": (
                bool,
                none_type,
            ),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None

    attribute_map = {
        "objects": "objects",  # noqa: E501
        "direct_cloud_archive": "directCloudArchive",  # noqa: E501
        "native_format": "nativeFormat",  # noqa: E501
        "indexing_policy": "indexingPolicy",  # noqa: E501
        "protocol": "protocol",  # noqa: E501
        "continue_on_error": "continueOnError",  # noqa: E501
        "encryption_enabled": "encryptionEnabled",  # noqa: E501
        "file_lock_config": "fileLockConfig",  # noqa: E501
        "file_filters": "fileFilters",  # noqa: E501
        "use_changelist": "useChangelist",  # noqa: E501
        "source_id": "sourceId",  # noqa: E501
        "source_name": "sourceName",  # noqa: E501
        "pre_post_script": "prePostScript",  # noqa: E501
        "continuous_snapshots": "continuousSnapshots",  # noqa: E501
        "filter_ip_config": "filterIpConfig",  # noqa: E501
        "throttling_config": "throttlingConfig",  # noqa: E501
        "modify_source_permissions": "modifySourcePermissions",  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set(
        [
            "_data_store",
            "_check_type",
            "_spec_property_naming",
            "_path_to_item",
            "_configuration",
            "_visited_composed_classes",
        ]
    )

    @convert_js_args_to_python_args
    def __init__(self, objects, *args, **kwargs):  # noqa: E501
        """IsilonProtectionGroupParams - a model defined in OpenAPI

        Args:
            objects ([IsilonProtectionGroupObjectParams]): Specifies the objects to be included in the Protection Group.

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

            direct_cloud_archive (bool, none_type): Specifies whether or not to store the snapshots in this run directly in an Archive Target instead of on the Cluster. If this is set to true, the associated policy must have exactly one Archive Target associated with it and the policy must be set up to archive after every run. Also, a Storage Domain cannot be specified. Default behavior is 'false'.. [optional]  # noqa: E501
            native_format (bool, none_type): Specifies whether or not to enable native format for direct archive job. This field is set to true if native format should be used for archiving.. [optional]  # noqa: E501
            indexing_policy (IndexingPolicy): [optional]  # noqa: E501
            protocol (str, none_type): Specifies the preferred protocol to use if this device supports multiple protocols.. [optional]  # noqa: E501
            continue_on_error (bool, none_type): Specifies whether or not the Protection Group should continue regardless of whether or not an error was encountered during protection group run.. [optional]  # noqa: E501
            encryption_enabled (bool, none_type): Specifies whether the protection group should use encryption while backup or not.. [optional]  # noqa: E501
            file_lock_config (FileLevelDataLockConfig): [optional]  # noqa: E501
            file_filters (FileFilteringPolicy): [optional]  # noqa: E501
            use_changelist (bool, none_type): Specify whether to use the Isilon Changelist API to directly discover changed files/directories for faster incremental backup. Cohesity will keep an extra snapshot which will be deleted by the next successful backup.. [optional]  # noqa: E501
            source_id (int, none_type): Specifies the id of the parent of the objects.. [optional]  # noqa: E501
            source_name (str, none_type): Specifies the name of the parent of the objects.. [optional]  # noqa: E501
            pre_post_script (HostBasedBackupScriptParams): [optional]  # noqa: E501
            continuous_snapshots (ContinuousSnapshotParams): [optional]  # noqa: E501
            filter_ip_config (FilterIpConfig): [optional]  # noqa: E501
            throttling_config (NasThrottlingConfig): [optional]  # noqa: E501
            modify_source_permissions (bool, none_type): Specifies if the Isilon source permissions should be modified internally to allow backups.. [optional]  # noqa: E501
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

        self.objects = objects
        for var_name, var_value in kwargs.items():
            if (
                var_name not in self.attribute_map
                and self._configuration is not None
                and self._configuration.discard_unknown_keys
                and self.additional_properties_type is None
            ):
                # discard variable.
                continue
            setattr(self, var_name, var_value)
