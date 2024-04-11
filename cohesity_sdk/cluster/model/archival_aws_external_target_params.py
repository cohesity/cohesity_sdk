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
    from cohesity_sdk.cluster.model.archival_aws_external_target_params_all_of import ArchivalAwsExternalTargetParamsAllOf
    from cohesity_sdk.cluster.model.aws_glacier_params import AwsGlacierParams
    from cohesity_sdk.cluster.model.aws_s3_glacier_deep_archive_params import AwsS3GlacierDeepArchiveParams
    from cohesity_sdk.cluster.model.aws_s3_glacier_ir_params import AwsS3GlacierIRParams
    from cohesity_sdk.cluster.model.aws_s3_glacier_params import AwsS3GlacierParams
    from cohesity_sdk.cluster.model.aws_s3_intelligent_params import AwsS3IntelligentParams
    from cohesity_sdk.cluster.model.aws_s3_one_zone_ia_params import AwsS3OneZoneIAParams
    from cohesity_sdk.cluster.model.aws_s3_standard_ia_params import AwsS3StandardIAParams
    from cohesity_sdk.cluster.model.aws_s3_standard_params import AwsS3StandardParams
    from cohesity_sdk.cluster.model.common_archival_aws_external_target_params import CommonArchivalAwsExternalTargetParams
    globals()['ArchivalAwsExternalTargetParamsAllOf'] = ArchivalAwsExternalTargetParamsAllOf
    globals()['AwsGlacierParams'] = AwsGlacierParams
    globals()['AwsS3GlacierDeepArchiveParams'] = AwsS3GlacierDeepArchiveParams
    globals()['AwsS3GlacierIRParams'] = AwsS3GlacierIRParams
    globals()['AwsS3GlacierParams'] = AwsS3GlacierParams
    globals()['AwsS3IntelligentParams'] = AwsS3IntelligentParams
    globals()['AwsS3OneZoneIAParams'] = AwsS3OneZoneIAParams
    globals()['AwsS3StandardIAParams'] = AwsS3StandardIAParams
    globals()['AwsS3StandardParams'] = AwsS3StandardParams
    globals()['CommonArchivalAwsExternalTargetParams'] = CommonArchivalAwsExternalTargetParams


class ArchivalAwsExternalTargetParams(ModelComposed):
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
        ('storage_class',): {
            'None': None,
            'AMAZONS3STANDARD': "AmazonS3Standard",
            'AMAZONS3STANDARDIA': "AmazonS3StandardIA",
            'AMAZONS3ONEZONEIA': "AmazonS3OneZoneIA",
            'AMAZONS3INTELLIGENTTIERING': "AmazonS3IntelligentTiering",
            'AMAZONS3GLACIER': "AmazonS3Glacier",
            'AMAZONS3GLACIERDEEPARCHIVE': "AmazonS3GlacierDeepArchive",
            'AMAZONGLACIER': "AmazonGlacier",
            'AMAZONS3GLACIERIR': "AmazonS3GlacierIR",
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
            'bucket_name': (str, none_type,),  # noqa: E501
            'region': (str, none_type,),  # noqa: E501
            'storage_class': (str, none_type,),  # noqa: E501
            'is_forever_incremental_archival_enabled': (bool, none_type,),  # noqa: E501
            'is_incremental_archival_enabled': (bool, none_type,),  # noqa: E501
            'source_side_deduplication': (bool, none_type,),  # noqa: E501
            'aws_glacier_params': (AwsGlacierParams,),  # noqa: E501
            'aws_s3_glacier_deep_archive_params': (AwsS3GlacierDeepArchiveParams,),  # noqa: E501
            'aws_s3_glacier_ir_params': (AwsS3GlacierIRParams,),  # noqa: E501
            'aws_s3_glacier_params': (AwsS3GlacierParams,),  # noqa: E501
            'aws_s3_intelligent_params': (AwsS3IntelligentParams,),  # noqa: E501
            'aws_s3_one_zone_ia_params': (AwsS3OneZoneIAParams,),  # noqa: E501
            'aws_s3_standard_ia_params': (AwsS3StandardIAParams,),  # noqa: E501
            'aws_s3_standard_params': (AwsS3StandardParams,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None



    attribute_map = {
        'bucket_name': 'bucketName',  # noqa: E501
        'region': 'region',  # noqa: E501
        'storage_class': 'storageClass',  # noqa: E501
        'is_forever_incremental_archival_enabled': 'isForeverIncrementalArchivalEnabled',  # noqa: E501
        'is_incremental_archival_enabled': 'isIncrementalArchivalEnabled',  # noqa: E501
        'source_side_deduplication': 'sourceSideDeduplication',  # noqa: E501
        'aws_glacier_params': 'awsGlacierParams',  # noqa: E501
        'aws_s3_glacier_deep_archive_params': 'awsS3GlacierDeepArchiveParams',  # noqa: E501
        'aws_s3_glacier_ir_params': 'awsS3GlacierIRParams',  # noqa: E501
        'aws_s3_glacier_params': 'awsS3GlacierParams',  # noqa: E501
        'aws_s3_intelligent_params': 'awsS3IntelligentParams',  # noqa: E501
        'aws_s3_one_zone_ia_params': 'awsS3OneZoneIAParams',  # noqa: E501
        'aws_s3_standard_ia_params': 'awsS3StandardIAParams',  # noqa: E501
        'aws_s3_standard_params': 'awsS3StandardParams',  # noqa: E501
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
    def __init__(self, bucket_name, region, storage_class, *args, **kwargs):  # noqa: E501
        """ArchivalAwsExternalTargetParams - a model defined in OpenAPI

        Args:
            bucket_name (str, none_type): Specifies bucket name of the External Target.
            region (str, none_type): Specifies region of the External Target.
            storage_class (str, none_type): Specifies the AWS External Target storage class.

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

            is_forever_incremental_archival_enabled (bool, none_type): Specifies if Forever Incremental Archival setting is enabled or not.. [optional]  # noqa: E501
            is_incremental_archival_enabled (bool, none_type): Specifies if Incremental Archival setting is enabled or not.. [optional]  # noqa: E501
            source_side_deduplication (bool, none_type): Specifies the Source Side Deduplication setting for the AWS external target. [optional]  # noqa: E501
            aws_glacier_params (AwsGlacierParams): [optional]  # noqa: E501
            aws_s3_glacier_deep_archive_params (AwsS3GlacierDeepArchiveParams): [optional]  # noqa: E501
            aws_s3_glacier_ir_params (AwsS3GlacierIRParams): [optional]  # noqa: E501
            aws_s3_glacier_params (AwsS3GlacierParams): [optional]  # noqa: E501
            aws_s3_intelligent_params (AwsS3IntelligentParams): [optional]  # noqa: E501
            aws_s3_one_zone_ia_params (AwsS3OneZoneIAParams): [optional]  # noqa: E501
            aws_s3_standard_ia_params (AwsS3StandardIAParams): [optional]  # noqa: E501
            aws_s3_standard_params (AwsS3StandardParams): [optional]  # noqa: E501
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
            'bucket_name': bucket_name,
            'region': region,
            'storage_class': storage_class,
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
              ArchivalAwsExternalTargetParamsAllOf,
              CommonArchivalAwsExternalTargetParams,
          ],
          'oneOf': [
          ],
        }

