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
    from cohesity_sdk.cluster.model.archival_aws_external_target_params import ArchivalAwsExternalTargetParams
    from cohesity_sdk.cluster.model.archival_azure_external_target_params import ArchivalAzureExternalTargetParams
    from cohesity_sdk.cluster.model.archival_external_target_params_all_of import ArchivalExternalTargetParamsAllOf
    from cohesity_sdk.cluster.model.archival_gcp_external_target_params import ArchivalGcpExternalTargetParams
    from cohesity_sdk.cluster.model.archival_nas_external_target_params import ArchivalNasExternalTargetParams
    from cohesity_sdk.cluster.model.archival_oracle_external_target_params import ArchivalOracleExternalTargetParams
    from cohesity_sdk.cluster.model.archival_qstar_tape_external_target_params import ArchivalQstarTapeExternalTargetParams
    from cohesity_sdk.cluster.model.archival_s3_comp_external_target_params import ArchivalS3CompExternalTargetParams
    from cohesity_sdk.cluster.model.common_archival_external_target_params import CommonArchivalExternalTargetParams
    from cohesity_sdk.cluster.model.encryption_settings import EncryptionSettings
    from cohesity_sdk.cluster.model.target_bandwidth_throttlings import TargetBandwidthThrottlings
    globals()['ArchivalAwsExternalTargetParams'] = ArchivalAwsExternalTargetParams
    globals()['ArchivalAzureExternalTargetParams'] = ArchivalAzureExternalTargetParams
    globals()['ArchivalExternalTargetParamsAllOf'] = ArchivalExternalTargetParamsAllOf
    globals()['ArchivalGcpExternalTargetParams'] = ArchivalGcpExternalTargetParams
    globals()['ArchivalNasExternalTargetParams'] = ArchivalNasExternalTargetParams
    globals()['ArchivalOracleExternalTargetParams'] = ArchivalOracleExternalTargetParams
    globals()['ArchivalQstarTapeExternalTargetParams'] = ArchivalQstarTapeExternalTargetParams
    globals()['ArchivalS3CompExternalTargetParams'] = ArchivalS3CompExternalTargetParams
    globals()['CommonArchivalExternalTargetParams'] = CommonArchivalExternalTargetParams
    globals()['EncryptionSettings'] = EncryptionSettings
    globals()['TargetBandwidthThrottlings'] = TargetBandwidthThrottlings


class ArchivalExternalTargetParams(ModelComposed):
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
        ('storage_type',): {
            'None': None,
            'AZURE': "Azure",
            'GOOGLE': "Google",
            'AWS': "AWS",
            'ORACLE': "Oracle",
            'NAS': "NAS",
            'QSTARTAPE': "QStarTape",
            'S3COMPATIBLE': "S3Compatible",
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
            'encryption': (EncryptionSettings,),  # noqa: E501
            'storage_type': (str, none_type,),  # noqa: E501
            'target_bandwidth_throttlings': (TargetBandwidthThrottlings,),  # noqa: E501
            'aws_params': (ArchivalAwsExternalTargetParams,),  # noqa: E501
            'azure_params': (ArchivalAzureExternalTargetParams,),  # noqa: E501
            'gcp_params': (ArchivalGcpExternalTargetParams,),  # noqa: E501
            'nas_params': (ArchivalNasExternalTargetParams,),  # noqa: E501
            'oracle_params': (ArchivalOracleExternalTargetParams,),  # noqa: E501
            'qstar_tape_params': (ArchivalQstarTapeExternalTargetParams,),  # noqa: E501
            's3_comp_params': (ArchivalS3CompExternalTargetParams,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None



    attribute_map = {
        'encryption': 'encryption',  # noqa: E501
        'storage_type': 'storageType',  # noqa: E501
        'target_bandwidth_throttlings': 'targetBandwidthThrottlings',  # noqa: E501
        'aws_params': 'awsParams',  # noqa: E501
        'azure_params': 'azureParams',  # noqa: E501
        'gcp_params': 'gcpParams',  # noqa: E501
        'nas_params': 'nasParams',  # noqa: E501
        'oracle_params': 'oracleParams',  # noqa: E501
        'qstar_tape_params': 'qstarTapeParams',  # noqa: E501
        's3_comp_params': 's3CompParams',  # noqa: E501
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
    def __init__(self, encryption, storage_type, *args, **kwargs):  # noqa: E501
        """ArchivalExternalTargetParams - a model defined in OpenAPI

        Args:
            encryption (EncryptionSettings):
            storage_type (str, none_type): Specifies the Storage type of the External Target.

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

            target_bandwidth_throttlings (TargetBandwidthThrottlings): [optional]  # noqa: E501
            aws_params (ArchivalAwsExternalTargetParams): [optional]  # noqa: E501
            azure_params (ArchivalAzureExternalTargetParams): [optional]  # noqa: E501
            gcp_params (ArchivalGcpExternalTargetParams): [optional]  # noqa: E501
            nas_params (ArchivalNasExternalTargetParams): [optional]  # noqa: E501
            oracle_params (ArchivalOracleExternalTargetParams): [optional]  # noqa: E501
            qstar_tape_params (ArchivalQstarTapeExternalTargetParams): [optional]  # noqa: E501
            s3_comp_params (ArchivalS3CompExternalTargetParams): [optional]  # noqa: E501
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
            'encryption': encryption,
            'storage_type': storage_type,
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
              ArchivalExternalTargetParamsAllOf,
              CommonArchivalExternalTargetParams,
          ],
          'oneOf': [
          ],
        }

