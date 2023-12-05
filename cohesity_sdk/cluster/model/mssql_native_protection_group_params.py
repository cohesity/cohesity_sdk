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
    from cohesity_sdk.cluster.model.common_mssql_protection_group_params import CommonMSSQLProtectionGroupParams
    from cohesity_sdk.cluster.model.filter import Filter
    from cohesity_sdk.cluster.model.mssql_native_protection_group_object_params import MSSQLNativeProtectionGroupObjectParams
    from cohesity_sdk.cluster.model.mssql_native_protection_group_params_all_of import MSSQLNativeProtectionGroupParamsAllOf
    from cohesity_sdk.cluster.model.pre_post_script_params import PrePostScriptParams
    globals()['CommonMSSQLProtectionGroupParams'] = CommonMSSQLProtectionGroupParams
    globals()['Filter'] = Filter
    globals()['MSSQLNativeProtectionGroupObjectParams'] = MSSQLNativeProtectionGroupObjectParams
    globals()['MSSQLNativeProtectionGroupParamsAllOf'] = MSSQLNativeProtectionGroupParamsAllOf
    globals()['PrePostScriptParams'] = PrePostScriptParams


class MSSQLNativeProtectionGroupParams(ModelComposed):
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
        ('aag_backup_preference_type',): {
            'None': None,
            'KPRIMARYREPLICAONLY': "kPrimaryReplicaOnly",
            'KSECONDARYREPLICAONLY': "kSecondaryReplicaOnly",
            'KPREFERSECONDARYREPLICA': "kPreferSecondaryReplica",
            'KANYREPLICA': "kAnyReplica",
        },
        ('user_db_backup_preference_type',): {
            'None': None,
            'KBACKUPALLDATABASES': "kBackupAllDatabases",
            'KBACKUPALLEXCEPTAAGDATABASES': "kBackupAllExceptAAGDatabases",
            'KBACKUPONLYAAGDATABASES': "kBackupOnlyAAGDatabases",
        },
    }

    validations = {
        ('objects',): {
            'min_items': 1,
        },

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
            'objects': ([MSSQLNativeProtectionGroupObjectParams], none_type,),  # noqa: E501
            'num_streams': (int, none_type,),  # noqa: E501
            'with_clause': (str, none_type,),  # noqa: E501
            'aag_backup_preference_type': (str, none_type,),  # noqa: E501
            'backup_system_dbs': (bool, none_type,),  # noqa: E501
            'exclude_filters': ([Filter], none_type,),  # noqa: E501
            'full_backups_copy_only': (bool, none_type,),  # noqa: E501
            'log_backup_num_streams': (int, none_type,),  # noqa: E501
            'log_backup_with_clause': (str, none_type,),  # noqa: E501
            'pre_post_script': (PrePostScriptParams,),  # noqa: E501
            'use_aag_preferences_from_server': (bool, none_type,),  # noqa: E501
            'user_db_backup_preference_type': (str, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None



    attribute_map = {
        'objects': 'objects',  # noqa: E501
        'num_streams': 'numStreams',  # noqa: E501
        'with_clause': 'withClause',  # noqa: E501
        'aag_backup_preference_type': 'aagBackupPreferenceType',  # noqa: E501
        'backup_system_dbs': 'backupSystemDbs',  # noqa: E501
        'exclude_filters': 'excludeFilters',  # noqa: E501
        'full_backups_copy_only': 'fullBackupsCopyOnly',  # noqa: E501
        'log_backup_num_streams': 'logBackupNumStreams',  # noqa: E501
        'log_backup_with_clause': 'logBackupWithClause',  # noqa: E501
        'pre_post_script': 'prePostScript',  # noqa: E501
        'use_aag_preferences_from_server': 'useAagPreferencesFromServer',  # noqa: E501
        'user_db_backup_preference_type': 'userDbBackupPreferenceType',  # noqa: E501
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
    def __init__(self, objects, *args, **kwargs):  # noqa: E501
        """MSSQLNativeProtectionGroupParams - a model defined in OpenAPI

        Args:
            objects ([MSSQLNativeProtectionGroupObjectParams], none_type): Specifies the list of object params to be protected.

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

            num_streams (int, none_type): Specifies the number of streams to be used.. [optional]  # noqa: E501
            with_clause (str, none_type): Specifies the WithClause to be used.. [optional]  # noqa: E501
            aag_backup_preference_type (str, none_type): Specifies the preference type for backing up databases that are part of an AAG. If not specified, then default preferences of the AAG server are applied. This field wont be applicable if user DB preference is set to skip AAG databases.. [optional]  # noqa: E501
            backup_system_dbs (bool, none_type): Specifies whether to backup system databases. If not specified then parameter is set to true.. [optional]  # noqa: E501
            exclude_filters ([Filter], none_type): Specifies the list of exclusion filters applied during the group creation or edit. These exclusion filters can be wildcard supported strings or regular expressions. Objects satisfying the will filters will be excluded during backup and also auto protected objects will be ignored if filtered by any of the filters.. [optional]  # noqa: E501
            full_backups_copy_only (bool, none_type): Specifies whether full backups should be copy-only.. [optional]  # noqa: E501
            log_backup_num_streams (int, none_type): Specifies the number of streams to be used for log backups.. [optional]  # noqa: E501
            log_backup_with_clause (str, none_type): Specifies the WithClause to be used for log backups.. [optional]  # noqa: E501
            pre_post_script (PrePostScriptParams): [optional]  # noqa: E501
            use_aag_preferences_from_server (bool, none_type): Specifies whether or not the AAG backup preferences specified on the SQL Server host should be used.. [optional]  # noqa: E501
            user_db_backup_preference_type (str, none_type): Specifies the preference type for backing up user databases on the host.. [optional]  # noqa: E501
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
            'objects': objects,
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
              CommonMSSQLProtectionGroupParams,
              MSSQLNativeProtectionGroupParamsAllOf,
          ],
          'oneOf': [
          ],
        }

