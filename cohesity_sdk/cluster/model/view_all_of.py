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
    from cohesity_sdk.cluster.model.file_count import FileCount
    from cohesity_sdk.cluster.model.view_alias_info import ViewAliasInfo
    from cohesity_sdk.cluster.model.view_failover import ViewFailover
    from cohesity_sdk.cluster.model.view_intent import ViewIntent
    from cohesity_sdk.cluster.model.view_protection import ViewProtection
    from cohesity_sdk.cluster.model.view_stats import ViewStats
    globals()['FileCount'] = FileCount
    globals()['ViewAliasInfo'] = ViewAliasInfo
    globals()['ViewFailover'] = ViewFailover
    globals()['ViewIntent'] = ViewIntent
    globals()['ViewProtection'] = ViewProtection
    globals()['ViewStats'] = ViewStats


class ViewAllOf(ModelNormal):
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
            'aliases': ([ViewAliasInfo], none_type,),  # noqa: E501
            'basic_mount_path': (str, none_type,),  # noqa: E501
            'case_insensitive_names_enabled': (bool, none_type,),  # noqa: E501
            'create_time_msecs': (int, none_type,),  # noqa: E501
            'data_lock_expiry_usecs': (int, none_type,),  # noqa: E501
            'file_count_by_size': ([FileCount], none_type,),  # noqa: E501
            'intent': (ViewIntent,),  # noqa: E501
            'is_category_inferred': (bool, none_type,),  # noqa: E501
            'is_target_for_migrated_data': (bool, none_type,),  # noqa: E501
            'nfs_mount_path': (str, none_type,),  # noqa: E501
            'nfs_mount_paths': ([str], none_type,),  # noqa: E501
            'object_services_mapping_config': (str, none_type,),  # noqa: E501
            'owner_sid': (str, none_type,),  # noqa: E501
            's3_folder_support_enabled': (bool, none_type,),  # noqa: E501
            'smb_mount_paths': ([str], none_type,),  # noqa: E501
            'stats': (ViewStats,),  # noqa: E501
            'storage_domain_id': (int, none_type,),  # noqa: E501
            'storage_domain_name': (str, none_type,),  # noqa: E501
            'view_failover': (ViewFailover,),  # noqa: E501
            'view_id': (int, none_type,),  # noqa: E501
            'view_protection': (ViewProtection,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None



    attribute_map = {
        'aliases': 'aliases',  # noqa: E501
        'basic_mount_path': 'basicMountPath',  # noqa: E501
        'case_insensitive_names_enabled': 'caseInsensitiveNamesEnabled',  # noqa: E501
        'create_time_msecs': 'createTimeMsecs',  # noqa: E501
        'data_lock_expiry_usecs': 'dataLockExpiryUsecs',  # noqa: E501
        'file_count_by_size': 'fileCountBySize',  # noqa: E501
        'intent': 'intent',  # noqa: E501
        'is_category_inferred': 'isCategoryInferred',  # noqa: E501
        'is_target_for_migrated_data': 'isTargetForMigratedData',  # noqa: E501
        'nfs_mount_path': 'nfsMountPath',  # noqa: E501
        'nfs_mount_paths': 'nfsMountPaths',  # noqa: E501
        'object_services_mapping_config': 'objectServicesMappingConfig',  # noqa: E501
        'owner_sid': 'ownerSid',  # noqa: E501
        's3_folder_support_enabled': 's3FolderSupportEnabled',  # noqa: E501
        'smb_mount_paths': 'smbMountPaths',  # noqa: E501
        'stats': 'stats',  # noqa: E501
        'storage_domain_id': 'storageDomainId',  # noqa: E501
        'storage_domain_name': 'storageDomainName',  # noqa: E501
        'view_failover': 'viewFailover',  # noqa: E501
        'view_id': 'viewId',  # noqa: E501
        'view_protection': 'viewProtection',  # noqa: E501
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
        """ViewAllOf - a model defined in OpenAPI

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

            aliases ([ViewAliasInfo], none_type): Aliases created for the view. A view alias allows a directory path inside a view to be mounted using the alias name.. [optional]  # noqa: E501
            basic_mount_path (str, none_type): Specifies the NFS mount path of the View (without the hostname information). This path is used to support NFS mounting of the paths specified in the nfsExportPathList on Windows systems.. [optional]  # noqa: E501
            case_insensitive_names_enabled (bool, none_type): Specifies whether to support case insensitive file/folder names. This parameter can only be set during create and cannot be changed.. [optional]  # noqa: E501
            create_time_msecs (int, none_type): Specifies the time that the View was created in milliseconds.. [optional]  # noqa: E501
            data_lock_expiry_usecs (int, none_type): DataLock (Write Once Read Many) lock expiry epoch time in microseconds. If a view is marked as a DataLock view, only a Data Security Officer (a user having Data Security Privilege) can delete the view until the lock expiry time.. [optional]  # noqa: E501
            file_count_by_size ([FileCount], none_type): Specifies the file count by size for the View.. [optional]  # noqa: E501
            intent (ViewIntent): [optional]  # noqa: E501
            is_category_inferred (bool, none_type): If True, category in response is not set by user but inferred by Iris because none is set. Category can only be none when view was created by v1 API or cloned from a view created by v1 API.  Inference Logic is as follows: 1. Object Services if only S3 or Swift protocol is selected. 2. Backup Target only if one read-write protocol is selected and    QoS is \"Backup Target Commvault\" or \"Backup Target SSD\". 3. File Services if there are more than 1 read-write protocol or    it doesn't fit any other category.. [optional]  # noqa: E501
            is_target_for_migrated_data (bool, none_type): Specifies if a view contains migrated data.. [optional]  # noqa: E501
            nfs_mount_path (str, none_type): This field is currently deprecated. Please use NFS MountPaths which would be an array of strings.. [optional]  # noqa: E501
            nfs_mount_paths ([str], none_type): Array of NFS Paths. Specifies the path for mounting this View as an NFS share. If Kerberos Provider has multiple hostaliases, each host alias has  its own path.. [optional]  # noqa: E501
            object_services_mapping_config (str, none_type): Specifies the Object Services key mapping config of the view. This parameter can only be set during create and cannot be changed. Configuration of Object Services key mapping. Specifies the type of Object Services key mapping config.. [optional]  # noqa: E501
            owner_sid (str, none_type): Specifies the sid of the view owner.. [optional]  # noqa: E501
            s3_folder_support_enabled (bool, none_type): Specifies whether to support s3 folder support feature. This parameter can only be set during create and cannot be changed.. [optional]  # noqa: E501
            smb_mount_paths ([str], none_type): Array of SMB Paths. Specifies the possible paths that can be used to mount this View as a SMB share. If Active Directory has multiple account names; each machine account has its own path.. [optional]  # noqa: E501
            stats (ViewStats): [optional]  # noqa: E501
            storage_domain_id (int, none_type): Specifies the id of the Storage Domain (View Box) where the View is stored.. [optional]  # noqa: E501
            storage_domain_name (str, none_type): Specifies the name of the Storage Domain (View Box) where the View is stored.. [optional]  # noqa: E501
            view_failover (ViewFailover): [optional]  # noqa: E501
            view_id (int, none_type): Specifies an id of the View assigned by the Cohesity Cluster.. [optional]  # noqa: E501
            view_protection (ViewProtection): [optional]  # noqa: E501
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


