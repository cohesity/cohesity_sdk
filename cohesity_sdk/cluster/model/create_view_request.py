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
    from cohesity_sdk.cluster.model.create_view import CreateView
    from cohesity_sdk.cluster.model.subnet import Subnet
    from cohesity_sdk.cluster.model.view_protocol import ViewProtocol
    globals()['CreateView'] = CreateView
    globals()['Subnet'] = Subnet
    globals()['ViewProtocol'] = ViewProtocol


class CreateViewRequest(ModelComposed):
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
        ('object_services_mapping_config',): {
            'None': None,
            'RANDOM': "Random",
            'SHORT': "Short",
            'LONG': "Long",
            'HIERARCHICAL': "Hierarchical",
            'OBJECTID': "ObjectId",
        },
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
        ('versioning',): {
            'None': None,
            'UNVERSIONED': "UnVersioned",
            'ENABLED': "Enabled",
            'SUSPENDED': "Suspended",
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
            'storage_domain_id': (int, none_type,),  # noqa: E501
            'case_insensitive_names_enabled': (bool, none_type,),  # noqa: E501
            'object_services_mapping_config': (str, none_type,),  # noqa: E501
            'view_protection_config': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'intent': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            's3_folder_support_enabled': (bool, none_type,),  # noqa: E501
            'name': (str, none_type,),  # noqa: E501
            'category': (str, none_type,),  # noqa: E501
            'protocol_access': ([ViewProtocol], none_type,),  # noqa: E501
            'qos': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'override_global_subnet_whitelist': (bool, none_type,),  # noqa: E501
            'subnet_whitelist': ([Subnet], none_type,),  # noqa: E501
            'override_global_netgroup_whitelist': (bool, none_type,),  # noqa: E501
            'netgroup_whitelist': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'security_mode': (str, none_type,),  # noqa: E501
            'storage_policy_override': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'logical_quota': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'file_lock_config': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'file_extension_filter': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'antivirus_scan_config': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'description': (str, none_type,),  # noqa: E501
            'allow_mount_on_windows': (bool, none_type,),  # noqa: E501
            'enable_minion': (bool, none_type,),  # noqa: E501
            'enable_filer_audit_logging': (bool, none_type,),  # noqa: E501
            'tenant_id': (str, none_type,),  # noqa: E501
            'enable_live_indexing': (bool, none_type,),  # noqa: E501
            'enable_offline_caching': (bool, none_type,),  # noqa: E501
            'access_sids': ([str], none_type,),  # noqa: E501
            'view_lock_enabled': (bool, none_type,),  # noqa: E501
            'is_read_only': (bool, none_type,),  # noqa: E501
            'view_pinning_config': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'self_service_snapshot_config': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'enable_metadata_accelerator': (bool, none_type,),  # noqa: E501
            'is_externally_triggered_backup_target': (bool, none_type,),  # noqa: E501
            'enable_nfs_view_discovery': (bool, none_type,),  # noqa: E501
            'nfs_all_squash': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'nfs_root_permissions': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'nfs_root_squash': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'enable_nfs_unix_authentication': (bool, none_type,),  # noqa: E501
            'enable_nfs_kerberos_authentication': (bool, none_type,),  # noqa: E501
            'enable_nfs_kerberos_integrity': (bool, none_type,),  # noqa: E501
            'enable_nfs_kerberos_privacy': (bool, none_type,),  # noqa: E501
            'enable_smb_view_discovery': (bool, none_type,),  # noqa: E501
            'enable_smb_access_based_enumeration': (bool, none_type,),  # noqa: E501
            'enable_smb_encryption': (bool, none_type,),  # noqa: E501
            'enforce_smb_encryption': (bool, none_type,),  # noqa: E501
            'enable_fast_durable_handle': (bool, none_type,),  # noqa: E501
            'enable_smb_oplock': (bool, none_type,),  # noqa: E501
            'smb_permissions_info': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'share_permissions': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            's3_access_path': (str, none_type,),  # noqa: E501
            'acl_config': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'owner_info': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'versioning': (str, none_type,),  # noqa: E501
            'lifecycle_management': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'swift_project_domain': (str, none_type,),  # noqa: E501
            'swift_project_name': (str, none_type,),  # noqa: E501
            'swift_user_domain': (str, none_type,),  # noqa: E501
            'swift_username': (str, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None



    attribute_map = {
        'storage_domain_id': 'storageDomainId',  # noqa: E501
        'case_insensitive_names_enabled': 'caseInsensitiveNamesEnabled',  # noqa: E501
        'object_services_mapping_config': 'objectServicesMappingConfig',  # noqa: E501
        'view_protection_config': 'viewProtectionConfig',  # noqa: E501
        'intent': 'intent',  # noqa: E501
        's3_folder_support_enabled': 's3FolderSupportEnabled',  # noqa: E501
        'name': 'name',  # noqa: E501
        'category': 'category',  # noqa: E501
        'protocol_access': 'protocolAccess',  # noqa: E501
        'qos': 'qos',  # noqa: E501
        'override_global_subnet_whitelist': 'overrideGlobalSubnetWhitelist',  # noqa: E501
        'subnet_whitelist': 'subnetWhitelist',  # noqa: E501
        'override_global_netgroup_whitelist': 'overrideGlobalNetgroupWhitelist',  # noqa: E501
        'netgroup_whitelist': 'netgroupWhitelist',  # noqa: E501
        'security_mode': 'securityMode',  # noqa: E501
        'storage_policy_override': 'storagePolicyOverride',  # noqa: E501
        'logical_quota': 'logicalQuota',  # noqa: E501
        'file_lock_config': 'fileLockConfig',  # noqa: E501
        'file_extension_filter': 'fileExtensionFilter',  # noqa: E501
        'antivirus_scan_config': 'antivirusScanConfig',  # noqa: E501
        'description': 'description',  # noqa: E501
        'allow_mount_on_windows': 'allowMountOnWindows',  # noqa: E501
        'enable_minion': 'enableMinion',  # noqa: E501
        'enable_filer_audit_logging': 'enableFilerAuditLogging',  # noqa: E501
        'tenant_id': 'tenantId',  # noqa: E501
        'enable_live_indexing': 'enableLiveIndexing',  # noqa: E501
        'enable_offline_caching': 'enableOfflineCaching',  # noqa: E501
        'access_sids': 'accessSids',  # noqa: E501
        'view_lock_enabled': 'viewLockEnabled',  # noqa: E501
        'is_read_only': 'isReadOnly',  # noqa: E501
        'view_pinning_config': 'viewPinningConfig',  # noqa: E501
        'self_service_snapshot_config': 'selfServiceSnapshotConfig',  # noqa: E501
        'enable_metadata_accelerator': 'enableMetadataAccelerator',  # noqa: E501
        'is_externally_triggered_backup_target': 'isExternallyTriggeredBackupTarget',  # noqa: E501
        'enable_nfs_view_discovery': 'enableNfsViewDiscovery',  # noqa: E501
        'nfs_all_squash': 'nfsAllSquash',  # noqa: E501
        'nfs_root_permissions': 'nfsRootPermissions',  # noqa: E501
        'nfs_root_squash': 'nfsRootSquash',  # noqa: E501
        'enable_nfs_unix_authentication': 'enableNfsUnixAuthentication',  # noqa: E501
        'enable_nfs_kerberos_authentication': 'enableNfsKerberosAuthentication',  # noqa: E501
        'enable_nfs_kerberos_integrity': 'enableNfsKerberosIntegrity',  # noqa: E501
        'enable_nfs_kerberos_privacy': 'enableNfsKerberosPrivacy',  # noqa: E501
        'enable_smb_view_discovery': 'enableSmbViewDiscovery',  # noqa: E501
        'enable_smb_access_based_enumeration': 'enableSmbAccessBasedEnumeration',  # noqa: E501
        'enable_smb_encryption': 'enableSmbEncryption',  # noqa: E501
        'enforce_smb_encryption': 'enforceSmbEncryption',  # noqa: E501
        'enable_fast_durable_handle': 'enableFastDurableHandle',  # noqa: E501
        'enable_smb_oplock': 'enableSmbOplock',  # noqa: E501
        'smb_permissions_info': 'smbPermissionsInfo',  # noqa: E501
        'share_permissions': 'sharePermissions',  # noqa: E501
        's3_access_path': 's3AccessPath',  # noqa: E501
        'acl_config': 'aclConfig',  # noqa: E501
        'owner_info': 'ownerInfo',  # noqa: E501
        'versioning': 'versioning',  # noqa: E501
        'lifecycle_management': 'lifecycleManagement',  # noqa: E501
        'swift_project_domain': 'swiftProjectDomain',  # noqa: E501
        'swift_project_name': 'swiftProjectName',  # noqa: E501
        'swift_user_domain': 'swiftUserDomain',  # noqa: E501
        'swift_username': 'swiftUsername',  # noqa: E501
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
        """CreateViewRequest - a model defined in OpenAPI

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

            storage_domain_id (int, none_type): Specifies the id of the Storage Domain (View Box) where the View will be created.. [optional]  # noqa: E501
            case_insensitive_names_enabled (bool, none_type): Specifies whether to support case insensitive file/folder names. This parameter can only be set during create and cannot be changed.. [optional]  # noqa: E501
            object_services_mapping_config (str, none_type): Specifies the Object Services key mapping config of the view. This parameter can only be set during create and cannot be changed. Configuration of Object Services key mapping. Specifies the type of Object Services key mapping config.. [optional]  # noqa: E501
            view_protection_config ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Specifies the protection config of the View.. [optional]  # noqa: E501
            intent ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Specifies the intent of the View.. [optional]  # noqa: E501
            s3_folder_support_enabled (bool, none_type): Specifies whether to support s3 folder support feature. This parameter can only be set during create and cannot be changed.. [optional]  # noqa: E501
            name (str, none_type): Specifies the name of the View.. [optional]  # noqa: E501
            category (str, none_type): Specifies the category of the View.. [optional]  # noqa: E501
            protocol_access ([ViewProtocol], none_type): Specifies the supported Protocols for the View.. [optional]  # noqa: E501
            qos ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Specifies the Quality of Service (QoS) Policy for the View.. [optional]  # noqa: E501
            override_global_subnet_whitelist (bool, none_type): Specifies whether view level client subnet whitelist overrides cluster and global setting.. [optional]  # noqa: E501
            subnet_whitelist ([Subnet], none_type): Array of Subnets. Specifies a list of Subnets with IP addresses that have permissions to access the View. (Overrides or extends the Subnets specified at the global Cohesity Cluster level.). [optional]  # noqa: E501
            override_global_netgroup_whitelist (bool, none_type): Specifies whether view level client netgroup whitelist overrides cluster and global setting.. [optional]  # noqa: E501
            netgroup_whitelist ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Array of Netgroups. Specifies a list of netgroups with domains that have permissions to access the View. (Overrides or extends the Netgroup specified at the global Cohesity Cluster level.). [optional]  # noqa: E501
            security_mode (str, none_type): Specifies the security mode used for this view. Currently we support the following modes: Native, Unified and NTFS style. 'NativeMode' indicates a native security mode. 'UnifiedMode' indicates a unified security mode. 'NtfsMode' indicates a NTFS style security mode.. [optional]  # noqa: E501
            storage_policy_override ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Specifies if inline deduplication and compression settings inherited from the Storage Domain (View Box) should be disabled for this View.. [optional]  # noqa: E501
            logical_quota ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Specifies an optional logical quota limit (in bytes) for the usage allowed on this View. (Logical data is when the data is fully hydrated and expanded.) This limit overrides the limit inherited from the Storage Domain (View Box) (if set). If logicalQuota is nil, the limit is inherited from the Storage Domain (View Box) (if set). A new write is not allowed if the Storage Domain (View Box) will exceed the specified quota. However, it takes time for the Cohesity Cluster to calculate the usage across Nodes, so the limit may be exceeded by a small amount. In addition, if the limit is increased or data is removed, there may be a delay before the Cohesity Cluster allows more data to be written to the View, as the Cluster is calculating the usage across Nodes.. [optional]  # noqa: E501
            file_lock_config ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Optional config that enables file locking for this view. It cannot be disabled during the edit of a view, if it has been enabled during the creation of the view. Also, it cannot be enabled if it was disabled during the creation of the view.. [optional]  # noqa: E501
            file_extension_filter ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Optional filtering criteria that should be satisfied by all the files created in this view. It does not affect existing files.. [optional]  # noqa: E501
            antivirus_scan_config ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Specifies the antivirus scan config settings for this View.. [optional]  # noqa: E501
            description (str, none_type): Specifies an optional text description about the View.. [optional]  # noqa: E501
            allow_mount_on_windows (bool, none_type): Specifies if this View can be mounted using the NFS protocol on Windows systems. If true, this View can be NFS mounted on Windows systems.. [optional]  # noqa: E501
            enable_minion (bool, none_type): Specifies if this view should allow minion or not. If true, this will allow minion.. [optional]  # noqa: E501
            enable_filer_audit_logging (bool, none_type): Specifies if Filer Audit Logging is enabled for this view.. [optional]  # noqa: E501
            tenant_id (str, none_type): Optional tenant id who has access to this View.. [optional]  # noqa: E501
            enable_live_indexing (bool, none_type): Specifies whether to enable live indexing for the view.. [optional]  # noqa: E501
            enable_offline_caching (bool, none_type): Specifies whether to enable offline file caching of the view.. [optional]  # noqa: E501
            access_sids ([str], none_type): Array of Security Identifiers (SIDs) Specifies the list of security identifiers (SIDs) for the restricted Principals who have access to this View.. [optional]  # noqa: E501
            view_lock_enabled (bool, none_type): Specifies whether view lock is enabled. If enabled the view cannot be modified or deleted until unlock. By default it is disabled.. [optional]  # noqa: E501
            is_read_only (bool, none_type): Specifies if the view is a read only view. User will no longer be able to write to this view if this is set to true.. [optional]  # noqa: E501
            view_pinning_config ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Specifies the pinning config of this view.. [optional]  # noqa: E501
            self_service_snapshot_config ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Specifies self service config of this view.. [optional]  # noqa: E501
            enable_metadata_accelerator (bool, none_type): Specifies if metadata accelerator is enabled for this view. Only supported while creating a view.. [optional]  # noqa: E501
            is_externally_triggered_backup_target (bool, none_type): Specifies whether the view is for externally triggered backup target. If so, Magneto will ignore the backup schedule for the view protection job of this view. By default it is disabled.. [optional]  # noqa: E501
            enable_nfs_view_discovery (bool, none_type): If set, it enables discovery of view for NFS.. [optional]  # noqa: E501
            nfs_all_squash ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Specifies the NFS all squash config.. [optional]  # noqa: E501
            nfs_root_permissions ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Specifies the NFS root permission config of the view file system.. [optional]  # noqa: E501
            nfs_root_squash ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Specifies the NFS root squash config.. [optional]  # noqa: E501
            enable_nfs_unix_authentication (bool, none_type): If set, it enables NFS UNIX Authentication. [optional]  # noqa: E501
            enable_nfs_kerberos_authentication (bool, none_type): If set, it enables NFS Kerberos Authentication. [optional]  # noqa: E501
            enable_nfs_kerberos_integrity (bool, none_type): If set, it enables NFS Kerberos Integrity. [optional]  # noqa: E501
            enable_nfs_kerberos_privacy (bool, none_type): If set, it enables NFS Kerberos Privacy. [optional]  # noqa: E501
            enable_smb_view_discovery (bool, none_type): If set, it enables discovery of view for SMB.. [optional]  # noqa: E501
            enable_smb_access_based_enumeration (bool, none_type): Specifies if access-based enumeration should be enabled. If 'true', only files and folders that the user has permissions to access are visible on the SMB share for that user.. [optional]  # noqa: E501
            enable_smb_encryption (bool, none_type): Specifies the SMB encryption for the View. If set, it enables the SMB encryption for the View. Encryption is supported only by SMB 3.x dialects. Dialects that do not support would still access data in unencrypted format.. [optional]  # noqa: E501
            enforce_smb_encryption (bool, none_type): Specifies the SMB encryption for all the sessions for the View. If set, encryption is enforced for all the sessions for the View. When enabled all future and existing unencrypted sessions are disallowed.. [optional]  # noqa: E501
            enable_fast_durable_handle (bool, none_type): Specifies whether fast durable handle is enabled. If enabled, view open handle will be kept in memory, which results in a higher performance. But the handles cannot be recovered if node or service crashes.. [optional]  # noqa: E501
            enable_smb_oplock (bool, none_type): Specifies whether SMB opportunistic lock is enabled.. [optional]  # noqa: E501
            smb_permissions_info ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Specifies the SMB permissions for the View.. [optional]  # noqa: E501
            share_permissions ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Specifies share level permissions of the view.. [optional]  # noqa: E501
            s3_access_path (str, none_type): Specifies the path to access this View as an S3 share.. [optional]  # noqa: E501
            acl_config ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Specifies the ACL config of the View as an S3 bucket.. [optional]  # noqa: E501
            owner_info ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Specifies the owner info of the View as an S3 bucket.. [optional]  # noqa: E501
            versioning (str, none_type): Specifies the versioning state of S3 bucket. Buckets can be in one of three states: UnVersioned (default), VersioningEnabled, or VersioningSuspended. Once versioning is enabled for a bucket, it can never return to an UnVersioned state. However, versioning on the bucket can be suspended.. [optional]  # noqa: E501
            lifecycle_management ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Specifies the S3 Lifecycle policy of the bucket. [optional]  # noqa: E501
            swift_project_domain (str, none_type): Specifies the Keystone project domain.. [optional]  # noqa: E501
            swift_project_name (str, none_type): Specifies the Keystone project name.. [optional]  # noqa: E501
            swift_user_domain (str, none_type): Specifies the Keystone user domain.. [optional]  # noqa: E501
            swift_username (str, none_type): Specifies the Keystone username.. [optional]  # noqa: E501
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
              CreateView,
          ],
          'oneOf': [
          ],
        }

