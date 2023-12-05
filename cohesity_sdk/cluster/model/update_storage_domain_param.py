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
    from cohesity_sdk.cluster.model.schema import Schema
    from cohesity_sdk.cluster.model.storage_domain import StorageDomain
    from cohesity_sdk.cluster.model.subnet import Subnet
    globals()['FileCount'] = FileCount
    globals()['Schema'] = Schema
    globals()['StorageDomain'] = StorageDomain
    globals()['Subnet'] = Subnet


class UpdateStorageDomainParam(ModelComposed):
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
            'cluster_partition_id': (int, none_type,),  # noqa: E501
            'name': (str, none_type,),  # noqa: E501
            'ad_domain_name': (str, none_type,),  # noqa: E501
            'blob_brick_size_bytes': (int, none_type,),  # noqa: E501
            'cloud_domain_id': (int, none_type,),  # noqa: E501
            'cloud_down_water_fall_params': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'cluster_partition_name': (str, none_type,),  # noqa: E501
            'default_user_quota': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'default_view_quota': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'dek_rotation_enabled': (bool, none_type,),  # noqa: E501
            'direct_archive_enabled': (bool, none_type,),  # noqa: E501
            'file_count_by_size': ([FileCount], none_type,),  # noqa: E501
            'id': (int, none_type,),  # noqa: E501
            'kerberos_realm_name': (str, none_type,),  # noqa: E501
            'kms_server_id': (int, none_type,),  # noqa: E501
            'ldap_provider_id': (int, none_type,),  # noqa: E501
            'nis_domain_names': ([str], none_type,),  # noqa: E501
            'physical_quota': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'recommended': (bool, none_type,),  # noqa: E501
            's3_buckets_enabled': (bool, none_type,),  # noqa: E501
            'schemas': ([Schema], none_type,),  # noqa: E501
            'stats': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'storage_policy': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'subnet_whitelist': ([Subnet], none_type,),  # noqa: E501
            'tenant_ids': ([str], none_type,),  # noqa: E501
            'treat_file_sync_as_data_sync': (bool, none_type,),  # noqa: E501
            'vault_id': (int, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None



    attribute_map = {
        'cluster_partition_id': 'clusterPartitionId',  # noqa: E501
        'name': 'name',  # noqa: E501
        'ad_domain_name': 'adDomainName',  # noqa: E501
        'blob_brick_size_bytes': 'blobBrickSizeBytes',  # noqa: E501
        'cloud_domain_id': 'cloudDomainId',  # noqa: E501
        'cloud_down_water_fall_params': 'cloudDownWaterFallParams',  # noqa: E501
        'cluster_partition_name': 'clusterPartitionName',  # noqa: E501
        'default_user_quota': 'defaultUserQuota',  # noqa: E501
        'default_view_quota': 'defaultViewQuota',  # noqa: E501
        'dek_rotation_enabled': 'dekRotationEnabled',  # noqa: E501
        'direct_archive_enabled': 'directArchiveEnabled',  # noqa: E501
        'file_count_by_size': 'fileCountBySize',  # noqa: E501
        'id': 'id',  # noqa: E501
        'kerberos_realm_name': 'kerberosRealmName',  # noqa: E501
        'kms_server_id': 'kmsServerId',  # noqa: E501
        'ldap_provider_id': 'ldapProviderId',  # noqa: E501
        'nis_domain_names': 'nisDomainNames',  # noqa: E501
        'physical_quota': 'physicalQuota',  # noqa: E501
        'recommended': 'recommended',  # noqa: E501
        's3_buckets_enabled': 's3BucketsEnabled',  # noqa: E501
        'schemas': 'schemas',  # noqa: E501
        'stats': 'stats',  # noqa: E501
        'storage_policy': 'storagePolicy',  # noqa: E501
        'subnet_whitelist': 'subnetWhitelist',  # noqa: E501
        'tenant_ids': 'tenantIds',  # noqa: E501
        'treat_file_sync_as_data_sync': 'treatFileSyncAsDataSync',  # noqa: E501
        'vault_id': 'vaultId',  # noqa: E501
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
    def __init__(self, cluster_partition_id, name, *args, **kwargs):  # noqa: E501
        """UpdateStorageDomainParam - a model defined in OpenAPI

        Args:
            cluster_partition_id (int, none_type): Specifies the cluster partition id of the Storage Domain.
            name (str, none_type): Specifies the Storage Domain name.

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

            ad_domain_name (str, none_type): Specifies the Active Directory domain name that this Storage Domain is mapped to.. [optional]  # noqa: E501
            blob_brick_size_bytes (int, none_type): Specifies the brick size used for blobs in this Storage Domain.. [optional]  # noqa: E501
            cloud_domain_id (int, none_type): Specifies the cloud domain Id.. [optional]  # noqa: E501
            cloud_down_water_fall_params ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Specifies the cloud down water fall parameters for this Storage Domain.. [optional]  # noqa: E501
            cluster_partition_name (str, none_type): Specifies the cluster partition name of the Storage Domain.. [optional]  # noqa: E501
            default_user_quota ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Specifies a default user quota limit for users within views in this Storage Domain.. [optional]  # noqa: E501
            default_view_quota ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Specifies a default logical quota limit for all views in this Storage Domain. This quota can be overwritten by a view level quota.. [optional]  # noqa: E501
            dek_rotation_enabled (bool, none_type): Specifies whether DEK(Data Encryption Key) rotation is enabled for this Storage Domain. This is applicable only when the Storage Domain uses AWS or similar KMS in which the KEK (Key Encryption Key) is not created and maintained by Cohesity. For Internal KMS and keys stored in Safenet servers, DEK rotation will not be performed.. [optional]  # noqa: E501
            direct_archive_enabled (bool, none_type): Specifies whether to enable driect archive on this Storage Domain. If enabled, this Storage Domain can be used as a staging area while copying a large dataset that can't fit on the cluster to an external target.. [optional]  # noqa: E501
            file_count_by_size ([FileCount], none_type): Specifies the file count by size for the View.. [optional]  # noqa: E501
            id (int, none_type): Specifies the Storage Domain id.. [optional]  # noqa: E501
            kerberos_realm_name (str, none_type): Specifies the Kerberos realm name that this Storage Domain is mapped to.. [optional]  # noqa: E501
            kms_server_id (int, none_type): Specifies the associated KMS server id.. [optional]  # noqa: E501
            ldap_provider_id (int, none_type): Specifies the LDAP provider id that this Storage Domain is mapped to.. [optional]  # noqa: E501
            nis_domain_names ([str], none_type): Specifies the NIS domain names that this Storage Domain is mapped to.. [optional]  # noqa: E501
            physical_quota ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Specifies a quota limit for physical usage of this Storage Domain. This quota defines a limit of data that can be physically (after data size is reduced by block tracking, compression and deduplication) stored on this storage domain. A new write will not be allowed when the storage domain usage will exceeds the specified quota. Due to the latency of calculating usage across all nodes, the actual storage domain usage may exceed the quota limit by a little bit.. [optional]  # noqa: E501
            recommended (bool, none_type): Specifies whether Storage Domain is recommended for the specified View template.. [optional]  # noqa: E501
            s3_buckets_enabled (bool, none_type): Specifies whether to enable creation of S3 bucket on this Storage Domain.. [optional]  # noqa: E501
            schemas ([Schema], none_type): Specifies the Storage Domain schemas.. [optional]  # noqa: E501
            stats ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Specifies the Storage Domain stats.. [optional]  # noqa: E501
            storage_policy ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Specifies the storage policy for this Storage Domain.. [optional]  # noqa: E501
            subnet_whitelist ([Subnet], none_type): Specifies a list of Subnets with IP addresses that have permissions to access the Storage Domain.. [optional]  # noqa: E501
            tenant_ids ([str], none_type): Specifies a list of tenant ids that that Storage Domain belongs. There can only be one tenant id in this field unless Storage Domain sharing between tenants is allowed on this cluster.. [optional]  # noqa: E501
            treat_file_sync_as_data_sync (bool, none_type): If 'true', when the Cohesity Cluster is writing to a file, the file modification time is not persisted synchronously during the file write, so the modification time may not be accurate. (Typically the file modification time is off by 30 seconds but it can be longer.). [optional]  # noqa: E501
            vault_id (int, none_type): Specifies the vault Id associated with cloud domain ID.. [optional]  # noqa: E501
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
            'cluster_partition_id': cluster_partition_id,
            'name': name,
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
              StorageDomain,
          ],
          'oneOf': [
          ],
        }

