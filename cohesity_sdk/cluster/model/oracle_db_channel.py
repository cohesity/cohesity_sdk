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
    from cohesity_sdk.cluster.model.credentials import Credentials
    from cohesity_sdk.cluster.model.oracle_database_host import OracleDatabaseHost
    globals()['Credentials'] = Credentials
    globals()['OracleDatabaseHost'] = OracleDatabaseHost


class OracleDbChannel(ModelNormal):
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
        ('rman_backup_type',): {
            'KIMAGECOPY': "kImageCopy",
            'KBACKUPSETS': "kBackupSets",
            'KSBT': "kSbt",
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
            'archive_log_retention_days': (int, none_type,),  # noqa: E501
            'credentials': (Credentials,),  # noqa: E501
            'database_node_list': ([OracleDatabaseHost], none_type,),  # noqa: E501
            'database_unique_name': (str, none_type,),  # noqa: E501
            'database_uuid': (str, none_type,),  # noqa: E501
            'default_channel_count': (int, none_type,),  # noqa: E501
            'enable_dg_primary_backup': (bool, none_type,),  # noqa: E501
            'max_host_count': (int, none_type,),  # noqa: E501
            'rman_backup_type': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None



    attribute_map = {
        'archive_log_retention_days': 'archiveLogRetentionDays',  # noqa: E501
        'credentials': 'credentials',  # noqa: E501
        'database_node_list': 'databaseNodeList',  # noqa: E501
        'database_unique_name': 'databaseUniqueName',  # noqa: E501
        'database_uuid': 'databaseUuid',  # noqa: E501
        'default_channel_count': 'defaultChannelCount',  # noqa: E501
        'enable_dg_primary_backup': 'enableDgPrimaryBackup',  # noqa: E501
        'max_host_count': 'maxHostCount',  # noqa: E501
        'rman_backup_type': 'rmanBackupType',  # noqa: E501
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
        """OracleDbChannel - a model defined in OpenAPI

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

            archive_log_retention_days (int, none_type): Specifies the number of days archive log should be stored. For keeping the archived log forever, set this to -1. For deleting the archived log immediately, set this to 0. For deleting the archived log after n days, set this to n.. [optional]  # noqa: E501
            credentials (Credentials): [optional]  # noqa: E501
            database_node_list ([OracleDatabaseHost], none_type): Specifies the Node info from where we are allowed to take the backup/restore.. [optional]  # noqa: E501
            database_unique_name (str, none_type): Specifies the unique Name of the database.. [optional]  # noqa: E501
            database_uuid (str, none_type): Specifies the database unique id. This is an internal field and is filled by magneto master based on corresponding app entity id.. [optional]  # noqa: E501
            default_channel_count (int, none_type): Specifies the default number of channels to use per node per database. This value is used on all Oracle Database Nodes unless databaseNodeList item's channelCount is specified for the node. Default value for the number of channels will be calculated as the minimum of number of nodes in Cohesity cluster and 2 * number of CPU on the host. If the number of channels is unspecified here and unspecified within databaseNodeList, the above formula will be used to determine the same.. [optional]  # noqa: E501
            enable_dg_primary_backup (bool, none_type): Specifies whether the database having the Primary role within Data Guard configuration is to be backed up.. [optional]  # noqa: E501
            max_host_count (int, none_type): Specifies the maximum number of hosts from which backup/restore is allowed in parallel. This will be less than or equal to the number of databaseNode specified within databaseNodeList.. [optional]  # noqa: E501
            rman_backup_type (str): Specifies the type of Oracle RMAN backup requested. [optional]  # noqa: E501
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


