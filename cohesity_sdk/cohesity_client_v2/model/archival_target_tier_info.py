"""
    Cohesity REST API

    Cohesity API provides a RESTful interface to access the various data management operations on Cohesity cluster and Helios.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from cohesity_sdk.cohesity_client_v2.model_utils import (  # noqa: F401
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
    from cohesity_sdk.cohesity_client_v2.model.archival_target_tier_info_all_of import ArchivalTargetTierInfoAllOf
    from cohesity_sdk.cohesity_client_v2.model.aws_tiers import AWSTiers
    from cohesity_sdk.cohesity_client_v2.model.azure_tiers import AzureTiers
    from cohesity_sdk.cohesity_client_v2.model.google_tiers import GoogleTiers
    from cohesity_sdk.cohesity_client_v2.model.oracle_tiers import OracleTiers
    from cohesity_sdk.cohesity_client_v2.model.tier_level_settings import TierLevelSettings
    globals()['AWSTiers'] = AWSTiers
    globals()['ArchivalTargetTierInfoAllOf'] = ArchivalTargetTierInfoAllOf
    globals()['AzureTiers'] = AzureTiers
    globals()['GoogleTiers'] = GoogleTiers
    globals()['OracleTiers'] = OracleTiers
    globals()['TierLevelSettings'] = TierLevelSettings


class ArchivalTargetTierInfo(ModelComposed):
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
        ('cloud_platform',): {
            'None': None,
            'AWS': "AWS",
            'AZURE': "Azure",
            'ORACLE': "Oracle",
            'GOOGLE': "Google",
        },
        ('current_tier_type',): {
            'None': None,
            'KAMAZONS3STANDARD': "kAmazonS3Standard",
            'KAMAZONS3STANDARDIA': "kAmazonS3StandardIA",
            'KAMAZONS3ONEZONEIA': "kAmazonS3OneZoneIA",
            'KAMAZONS3INTELLIGENTTIERING': "kAmazonS3IntelligentTiering",
            'KAMAZONS3GLACIER': "kAmazonS3Glacier",
            'KAMAZONS3GLACIERDEEPARCHIVE': "kAmazonS3GlacierDeepArchive",
            'KAZURETIERHOT': "kAzureTierHot",
            'KAZURETIERCOOL': "kAzureTierCool",
            'KAZURETIERARCHIVE': "kAzureTierArchive",
            'KGOOGLESTANDARD': "kGoogleStandard",
            'KGOOGLEREGIONAL': "kGoogleRegional",
            'KGOOGLEMULTIREGIONAL': "kGoogleMultiRegional",
            'KGOOGLENEARLINE': "kGoogleNearline",
            'KGOOGLECOLDLINE': "kGoogleColdline",
            'KORACLETIERSTANDARD': "kOracleTierStandard",
            'KORACLETIERARCHIVE': "kOracleTierArchive",
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
            'cloud_platform': (str, none_type,),  # noqa: E501
            'aws_tiering': (AWSTiers,),  # noqa: E501
            'azure_tiering': (AzureTiers,),  # noqa: E501
            'google_tiering': (GoogleTiers,),  # noqa: E501
            'oracle_tiering': (OracleTiers,),  # noqa: E501
            'current_tier_type': (str, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None



    attribute_map = {
        'cloud_platform': 'cloudPlatform',  # noqa: E501
        'aws_tiering': 'awsTiering',  # noqa: E501
        'azure_tiering': 'azureTiering',  # noqa: E501
        'google_tiering': 'googleTiering',  # noqa: E501
        'oracle_tiering': 'oracleTiering',  # noqa: E501
        'current_tier_type': 'currentTierType',  # noqa: E501
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
    def __init__(self, cloud_platform, *args, **kwargs):  # noqa: E501
        """ArchivalTargetTierInfo - a model defined in OpenAPI

        Args:
            cloud_platform (str, none_type): Specifies the cloud platform to enable tiering.

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

            aws_tiering (AWSTiers): [optional]  # noqa: E501
            azure_tiering (AzureTiers): [optional]  # noqa: E501
            google_tiering (GoogleTiers): [optional]  # noqa: E501
            oracle_tiering (OracleTiers): [optional]  # noqa: E501
            current_tier_type (str, none_type): Specifies the type of the current tier where the snapshot resides. This will be specified if the run is a CAD run.. [optional]  # noqa: E501
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
            'cloud_platform': cloud_platform,
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
              ArchivalTargetTierInfoAllOf,
              TierLevelSettings,
          ],
          'oneOf': [
          ],
        }

