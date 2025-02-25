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
    from cohesity_sdk.cluster.model.antivirus_scan_config import AntivirusScanConfig
    from cohesity_sdk.cluster.model.file_extension_filter import FileExtensionFilter
    from cohesity_sdk.cluster.model.file_level_data_lock_config import FileLevelDataLockConfig
    from cohesity_sdk.cluster.model.filer_lifecycle_management import FilerLifecycleManagement
    from cohesity_sdk.cluster.model.nis_netgroups import NisNetgroups
    from cohesity_sdk.cluster.model.qo_s import QoS
    from cohesity_sdk.cluster.model.quota_policy import QuotaPolicy
    from cohesity_sdk.cluster.model.self_service_snapshot_config import SelfServiceSnapshotConfig
    from cohesity_sdk.cluster.model.storage_policy_override import StoragePolicyOverride
    from cohesity_sdk.cluster.model.subnet import Subnet
    from cohesity_sdk.cluster.model.view_pinning_config import ViewPinningConfig
    from cohesity_sdk.cluster.model.view_protocol import ViewProtocol
    globals()['AntivirusScanConfig'] = AntivirusScanConfig
    globals()['FileExtensionFilter'] = FileExtensionFilter
    globals()['FileLevelDataLockConfig'] = FileLevelDataLockConfig
    globals()['FilerLifecycleManagement'] = FilerLifecycleManagement
    globals()['NisNetgroups'] = NisNetgroups
    globals()['QoS'] = QoS
    globals()['QuotaPolicy'] = QuotaPolicy
    globals()['SelfServiceSnapshotConfig'] = SelfServiceSnapshotConfig
    globals()['StoragePolicyOverride'] = StoragePolicyOverride
    globals()['Subnet'] = Subnet
    globals()['ViewPinningConfig'] = ViewPinningConfig
    globals()['ViewProtocol'] = ViewProtocol


class UpdateViewParamAllOf(ModelNormal):
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
        ('category',): {
            'None': None,
            'BACKUPTARGET': "BackupTarget",
            'FILESERVICES': "FileServices",
            'OBJECTSERVICES': "ObjectServices",
        },
        ('security_mode',): {
            'None': None,
            'NATIVEMODE': "NativeMode",
            'UNIFIEDMODE': "UnifiedMode",
            'NTFSMODE': "NtfsMode",
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
            'access_sids': ([str], none_type,),  # noqa: E501
            'allow_mount_on_windows': (bool, none_type,),  # noqa: E501
            'antivirus_scan_config': (AntivirusScanConfig,),  # noqa: E501
            'category': (str, none_type,),  # noqa: E501
            'description': (str, none_type,),  # noqa: E501
            'enable_filer_audit_logging': (bool, none_type,),  # noqa: E501
            'enable_live_indexing': (bool, none_type,),  # noqa: E501
            'enable_metadata_accelerator': (bool, none_type,),  # noqa: E501
            'enable_minion': (bool, none_type,),  # noqa: E501
            'enable_offline_caching': (bool, none_type,),  # noqa: E501
            'file_extension_filter': (FileExtensionFilter,),  # noqa: E501
            'file_lock_config': (FileLevelDataLockConfig,),  # noqa: E501
            'filer_lifecycle_management': (FilerLifecycleManagement,),  # noqa: E501
            'is_externally_triggered_backup_target': (bool, none_type,),  # noqa: E501
            'is_read_only': (bool, none_type,),  # noqa: E501
            'lexicographic_prefetch': (bool, none_type,),  # noqa: E501
            'logical_quota': (QuotaPolicy,),  # noqa: E501
            'name': (str, none_type,),  # noqa: E501
            'netgroup_whitelist': (NisNetgroups,),  # noqa: E501
            'override_global_netgroup_whitelist': (bool, none_type,),  # noqa: E501
            'override_global_subnet_whitelist': (bool, none_type,),  # noqa: E501
            'protocol_access': ([ViewProtocol], none_type,),  # noqa: E501
            'qos': (QoS,),  # noqa: E501
            'security_mode': (str, none_type,),  # noqa: E501
            'self_service_snapshot_config': (SelfServiceSnapshotConfig,),  # noqa: E501
            'storage_policy_override': (StoragePolicyOverride,),  # noqa: E501
            'subnet_whitelist': ([Subnet], none_type,),  # noqa: E501
            'tenant_id': (str, none_type,),  # noqa: E501
            'view_lock_enabled': (bool, none_type,),  # noqa: E501
            'view_pinning_config': (ViewPinningConfig,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None



    attribute_map = {
        'access_sids': 'accessSids',  # noqa: E501
        'allow_mount_on_windows': 'allowMountOnWindows',  # noqa: E501
        'antivirus_scan_config': 'antivirusScanConfig',  # noqa: E501
        'category': 'category',  # noqa: E501
        'description': 'description',  # noqa: E501
        'enable_filer_audit_logging': 'enableFilerAuditLogging',  # noqa: E501
        'enable_live_indexing': 'enableLiveIndexing',  # noqa: E501
        'enable_metadata_accelerator': 'enableMetadataAccelerator',  # noqa: E501
        'enable_minion': 'enableMinion',  # noqa: E501
        'enable_offline_caching': 'enableOfflineCaching',  # noqa: E501
        'file_extension_filter': 'fileExtensionFilter',  # noqa: E501
        'file_lock_config': 'fileLockConfig',  # noqa: E501
        'filer_lifecycle_management': 'filerLifecycleManagement',  # noqa: E501
        'is_externally_triggered_backup_target': 'isExternallyTriggeredBackupTarget',  # noqa: E501
        'is_read_only': 'isReadOnly',  # noqa: E501
        'lexicographic_prefetch': 'lexicographicPrefetch',  # noqa: E501
        'logical_quota': 'logicalQuota',  # noqa: E501
        'name': 'name',  # noqa: E501
        'netgroup_whitelist': 'netgroupWhitelist',  # noqa: E501
        'override_global_netgroup_whitelist': 'overrideGlobalNetgroupWhitelist',  # noqa: E501
        'override_global_subnet_whitelist': 'overrideGlobalSubnetWhitelist',  # noqa: E501
        'protocol_access': 'protocolAccess',  # noqa: E501
        'qos': 'qos',  # noqa: E501
        'security_mode': 'securityMode',  # noqa: E501
        'self_service_snapshot_config': 'selfServiceSnapshotConfig',  # noqa: E501
        'storage_policy_override': 'storagePolicyOverride',  # noqa: E501
        'subnet_whitelist': 'subnetWhitelist',  # noqa: E501
        'tenant_id': 'tenantId',  # noqa: E501
        'view_lock_enabled': 'viewLockEnabled',  # noqa: E501
        'view_pinning_config': 'viewPinningConfig',  # noqa: E501
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
        """UpdateViewParamAllOf - a model defined in OpenAPI

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

            access_sids ([str], none_type): Array of Security Identifiers (SIDs) Specifies the list of security identifiers (SIDs) for the restricted Principals who have access to this View.. [optional]  # noqa: E501
            allow_mount_on_windows (bool, none_type): Specifies if this View can be mounted using the NFS protocol on Windows systems. If true, this View can be NFS mounted on Windows systems.. [optional]  # noqa: E501
            antivirus_scan_config (AntivirusScanConfig): [optional]  # noqa: E501
            category (str, none_type): Specifies the category of the View.. [optional]  # noqa: E501
            description (str, none_type): Specifies an optional text description about the View.. [optional]  # noqa: E501
            enable_filer_audit_logging (bool, none_type): Specifies if Filer Audit Logging is enabled for this view.. [optional]  # noqa: E501
            enable_live_indexing (bool, none_type): Specifies whether to enable live indexing for the view.. [optional]  # noqa: E501
            enable_metadata_accelerator (bool, none_type): Specifies if metadata accelerator is enabled for this view. Only supported while creating a view.. [optional]  # noqa: E501
            enable_minion (bool, none_type): Specifies if this view should allow minion or not. If true, this will allow minion.. [optional]  # noqa: E501
            enable_offline_caching (bool, none_type): Specifies whether to enable offline file caching of the view.. [optional]  # noqa: E501
            file_extension_filter (FileExtensionFilter): [optional]  # noqa: E501
            file_lock_config (FileLevelDataLockConfig): [optional]  # noqa: E501
            filer_lifecycle_management (FilerLifecycleManagement): [optional]  # noqa: E501
            is_externally_triggered_backup_target (bool, none_type): Specifies whether the view is for externally triggered backup target. If so, Magneto will ignore the backup schedule for the view protection job of this view. By default it is disabled.. [optional]  # noqa: E501
            is_read_only (bool, none_type): Specifies if the view is a read only view. User will no longer be able to write to this view if this is set to true.. [optional]  # noqa: E501
            lexicographic_prefetch (bool, none_type): If small files are accessed sequentially from a client, this specifies whether to detect and prefetch files based on the lexicographic index to improve file read performance.. [optional]  # noqa: E501
            logical_quota (QuotaPolicy): [optional]  # noqa: E501
            name (str, none_type): Specifies the name of the View.. [optional]  # noqa: E501
            netgroup_whitelist (NisNetgroups): [optional]  # noqa: E501
            override_global_netgroup_whitelist (bool, none_type): Specifies whether view level client netgroup whitelist overrides cluster and global setting.. [optional]  # noqa: E501
            override_global_subnet_whitelist (bool, none_type): Specifies whether view level client subnet whitelist overrides cluster and global setting.. [optional]  # noqa: E501
            protocol_access ([ViewProtocol], none_type): Specifies the supported Protocols for the View.. [optional]  # noqa: E501
            qos (QoS): [optional]  # noqa: E501
            security_mode (str, none_type): Specifies the security mode used for this view. Currently we support the following modes: Native, Unified and NTFS style. 'NativeMode' indicates a native security mode. 'UnifiedMode' indicates a unified security mode. 'NtfsMode' indicates a NTFS style security mode.. [optional]  # noqa: E501
            self_service_snapshot_config (SelfServiceSnapshotConfig): [optional]  # noqa: E501
            storage_policy_override (StoragePolicyOverride): [optional]  # noqa: E501
            subnet_whitelist ([Subnet], none_type): Array of Subnets. Specifies a list of Subnets with IP addresses that have permissions to access the View. (Overrides or extends the Subnets specified at the global Cohesity Cluster level.). [optional]  # noqa: E501
            tenant_id (str, none_type): Optional tenant id who has access to this View.. [optional]  # noqa: E501
            view_lock_enabled (bool, none_type): Specifies whether view lock is enabled. If enabled the view cannot be modified or deleted until unlock. By default it is disabled.. [optional]  # noqa: E501
            view_pinning_config (ViewPinningConfig): [optional]  # noqa: E501
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


