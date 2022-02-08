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
    from cohesity_sdk.helios.model.common_sql_app_source_config import CommonSqlAppSourceConfig
    from cohesity_sdk.helios.model.filename_pattern_to_directory import FilenamePatternToDirectory
    from cohesity_sdk.helios.model.multi_stage_restore_options import MultiStageRestoreOptions
    globals()['CommonSqlAppSourceConfig'] = CommonSqlAppSourceConfig
    globals()['FilenamePatternToDirectory'] = FilenamePatternToDirectory
    globals()['MultiStageRestoreOptions'] = MultiStageRestoreOptions


class RecoverSqlAppOriginalSourceConfig(ModelComposed):
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
        ('overwriting_policy',): {
            'None': None,
            'FAILIFEXISTS': "FailIfExists",
            'OVERWRITE': "Overwrite",
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
            'data_file_directory_location': (str, none_type,),  # noqa: E501
            'log_file_directory_location': (str, none_type,),  # noqa: E501
            'capture_tail_logs': (bool, none_type,),  # noqa: E501
            'new_database_name': (str, none_type,),  # noqa: E501
            'restore_time_usecs': (int, none_type,),  # noqa: E501
            'secondary_data_files_dir_list': ([FilenamePatternToDirectory], none_type,),  # noqa: E501
            'with_no_recovery': (bool, none_type,),  # noqa: E501
            'keep_cdc': (bool, none_type,),  # noqa: E501
            'overwriting_policy': (str, none_type,),  # noqa: E501
            'multi_stage_restore_options': (MultiStageRestoreOptions,),  # noqa: E501
            'native_recovery_with_clause': (str, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None



    attribute_map = {
        'data_file_directory_location': 'dataFileDirectoryLocation',  # noqa: E501
        'log_file_directory_location': 'logFileDirectoryLocation',  # noqa: E501
        'capture_tail_logs': 'captureTailLogs',  # noqa: E501
        'new_database_name': 'newDatabaseName',  # noqa: E501
        'restore_time_usecs': 'restoreTimeUsecs',  # noqa: E501
        'secondary_data_files_dir_list': 'secondaryDataFilesDirList',  # noqa: E501
        'with_no_recovery': 'withNoRecovery',  # noqa: E501
        'keep_cdc': 'keepCdc',  # noqa: E501
        'overwriting_policy': 'overwritingPolicy',  # noqa: E501
        'multi_stage_restore_options': 'multiStageRestoreOptions',  # noqa: E501
        'native_recovery_with_clause': 'nativeRecoveryWithClause',  # noqa: E501
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
        """RecoverSqlAppOriginalSourceConfig - a model defined in OpenAPI

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

            data_file_directory_location (str, none_type): Specifies the directory where to put the database data files. Missing directory will be automatically created. If you are overwriting the existing database then this field will be ignored.. [optional]  # noqa: E501
            log_file_directory_location (str, none_type): Specifies the directory where to put the database log files. Missing directory will be automatically created. If you are overwriting the existing database then this field will be ignored.. [optional]  # noqa: E501
            capture_tail_logs (bool, none_type): Set this to true if tail logs are to be captured before the recovery operation. This is only applicable if database is not being renamed.. [optional]  # noqa: E501
            new_database_name (str, none_type): Specifies a new name for the restored database. If this field is not specified, then the original database will be overwritten after recovery.. [optional]  # noqa: E501
            restore_time_usecs (int, none_type): Specifies the time in the past to which the Sql database needs to be restored. This allows for granular recovery of Sql databases. If this is not set, the Sql database will be restored from the full/incremental snapshot.. [optional]  # noqa: E501
            secondary_data_files_dir_list ([FilenamePatternToDirectory], none_type): Specifies the secondary data filename pattern and corresponding direcories of the DB. Secondary data files are optional and are user defined. The recommended file extention for secondary files is \".ndf\". If this option is specified and the destination folders do not exist they will be automatically created.. [optional]  # noqa: E501
            with_no_recovery (bool, none_type): Specifies the flag to bring DBs online or not after successful recovery. If this is passed as true, then it means DBs won't be brought online.. [optional]  # noqa: E501
            keep_cdc (bool, none_type): Specifies whether to keep CDC (Change Data Capture) on recovered databases or not. If not passed, this is assumed to be true. If withNoRecovery is passed as true, then this field must not be set to true. Passing this field as true in this scenario will be a invalid request.. [optional]  # noqa: E501
            overwriting_policy (str, none_type): Specifies a policy to be used while recovering existing databases.. [optional]  # noqa: E501
            multi_stage_restore_options (MultiStageRestoreOptions): [optional]  # noqa: E501
            native_recovery_with_clause (str, none_type): 'with_clause' contains 'with clause' to be used in native sql restore command. This is only applicable for database restore of native sql backup. Here user can specify multiple restore options. Example: 'WITH BUFFERCOUNT = 575, MAXTRANSFERSIZE = 2097152'.. [optional]  # noqa: E501
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
              CommonSqlAppSourceConfig,
          ],
          'oneOf': [
          ],
        }

