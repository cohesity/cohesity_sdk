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


class ViewsSummary(ModelNormal):
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
        return {
            'data_written_bytes': (int, none_type,),  # noqa: E501
            'data_written_bytes_prev': (int, none_type,),  # noqa: E501
            'data_written_bytes_prev_timestamp_usec': (int, none_type,),  # noqa: E501
            'data_written_bytes_timestamp_usec': (int, none_type,),  # noqa: E501
            'local_tier_resiliency_impact_bytes': (int, none_type,),  # noqa: E501
            'local_tier_resiliency_impact_bytes_prev': (int, none_type,),  # noqa: E501
            'local_tier_resiliency_impact_bytes_prev_timestamp_usec': (int, none_type,),  # noqa: E501
            'local_tier_resiliency_impact_bytes_timestamp_usec': (int, none_type,),  # noqa: E501
            'logical_usage_bytes': (int, none_type,),  # noqa: E501
            'logical_usage_bytes_prev': (int, none_type,),  # noqa: E501
            'logical_usage_bytes_prev_timestamp_usec': (int, none_type,),  # noqa: E501
            'logical_usage_bytes_timestamp_usec': (int, none_type,),  # noqa: E501
            'num_directories': (int, none_type,),  # noqa: E501
            'num_directories_prev': (int, none_type,),  # noqa: E501
            'num_files': (int, none_type,),  # noqa: E501
            'num_files_prev': (int, none_type,),  # noqa: E501
            'protected_views': (int, none_type,),  # noqa: E501
            'replicated_in_views': (int, none_type,),  # noqa: E501
            'replicated_out_views': (int, none_type,),  # noqa: E501
            'storage_consumed_bytes': (int, none_type,),  # noqa: E501
            'storage_consumed_bytes_prev': (int, none_type,),  # noqa: E501
            'storage_consumed_bytes_prev_timestamp_usec': (int, none_type,),  # noqa: E501
            'storage_consumed_bytes_timestamp_usec': (int, none_type,),  # noqa: E501
            'total_views': (int, none_type,),  # noqa: E501
            'view_entity_id': (str, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None



    attribute_map = {
        'data_written_bytes': 'dataWrittenBytes',  # noqa: E501
        'data_written_bytes_prev': 'dataWrittenBytesPrev',  # noqa: E501
        'data_written_bytes_prev_timestamp_usec': 'dataWrittenBytesPrevTimestampUsec',  # noqa: E501
        'data_written_bytes_timestamp_usec': 'dataWrittenBytesTimestampUsec',  # noqa: E501
        'local_tier_resiliency_impact_bytes': 'localTierResiliencyImpactBytes',  # noqa: E501
        'local_tier_resiliency_impact_bytes_prev': 'localTierResiliencyImpactBytesPrev',  # noqa: E501
        'local_tier_resiliency_impact_bytes_prev_timestamp_usec': 'localTierResiliencyImpactBytesPrevTimestampUsec',  # noqa: E501
        'local_tier_resiliency_impact_bytes_timestamp_usec': 'localTierResiliencyImpactBytesTimestampUsec',  # noqa: E501
        'logical_usage_bytes': 'logicalUsageBytes',  # noqa: E501
        'logical_usage_bytes_prev': 'logicalUsageBytesPrev',  # noqa: E501
        'logical_usage_bytes_prev_timestamp_usec': 'logicalUsageBytesPrevTimestampUsec',  # noqa: E501
        'logical_usage_bytes_timestamp_usec': 'logicalUsageBytesTimestampUsec',  # noqa: E501
        'num_directories': 'numDirectories',  # noqa: E501
        'num_directories_prev': 'numDirectoriesPrev',  # noqa: E501
        'num_files': 'numFiles',  # noqa: E501
        'num_files_prev': 'numFilesPrev',  # noqa: E501
        'protected_views': 'protectedViews',  # noqa: E501
        'replicated_in_views': 'replicatedInViews',  # noqa: E501
        'replicated_out_views': 'replicatedOutViews',  # noqa: E501
        'storage_consumed_bytes': 'storageConsumedBytes',  # noqa: E501
        'storage_consumed_bytes_prev': 'storageConsumedBytesPrev',  # noqa: E501
        'storage_consumed_bytes_prev_timestamp_usec': 'storageConsumedBytesPrevTimestampUsec',  # noqa: E501
        'storage_consumed_bytes_timestamp_usec': 'storageConsumedBytesTimestampUsec',  # noqa: E501
        'total_views': 'totalViews',  # noqa: E501
        'view_entity_id': 'viewEntityId',  # noqa: E501
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
        """ViewsSummary - a model defined in OpenAPI

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

            data_written_bytes (int, none_type): Specifies the data written to all the views in bytes.. [optional]  # noqa: E501
            data_written_bytes_prev (int, none_type): Specifies the data written to all the views in bytes at a specific time.. [optional]  # noqa: E501
            data_written_bytes_prev_timestamp_usec (int, none_type): Specifies the timestamp in micro seconds when 'dataWrittenBytesPrev' was calculated.. [optional]  # noqa: E501
            data_written_bytes_timestamp_usec (int, none_type): Specifies the timestamp in micro seconds when 'dataWrittenBytes' was calculated.. [optional]  # noqa: E501
            local_tier_resiliency_impact_bytes (int, none_type): Specifies the size of the data that has been replicated to other nodes as per RF or Erasure Coding policy.. [optional]  # noqa: E501
            local_tier_resiliency_impact_bytes_prev (int, none_type): Specifies the size of the data that has been replicated to other nodes as per RF or Erasure Coding policy at a specific time.. [optional]  # noqa: E501
            local_tier_resiliency_impact_bytes_prev_timestamp_usec (int, none_type): Specifies the timestamp in micro seconds when 'localTierResiliencyImpactBytesPrev' was calculated.. [optional]  # noqa: E501
            local_tier_resiliency_impact_bytes_timestamp_usec (int, none_type): Specifies the timestamp in micro seconds when 'localTierResiliencyImpactBytes' was calculated.. [optional]  # noqa: E501
            logical_usage_bytes (int, none_type): Specifies the logical usage of all the views in bytes.. [optional]  # noqa: E501
            logical_usage_bytes_prev (int, none_type): Specifies the logical usage of all the views in bytes at a specific time.. [optional]  # noqa: E501
            logical_usage_bytes_prev_timestamp_usec (int, none_type): Specifies the timestamp in micro seconds when 'logicalUsageBytesPrev' was calculated.. [optional]  # noqa: E501
            logical_usage_bytes_timestamp_usec (int, none_type): Specifies the timestamp in micro seconds when 'logicalUsageBytes' was calculated.. [optional]  # noqa: E501
            num_directories (int, none_type): Specifies the number of directories.. [optional]  # noqa: E501
            num_directories_prev (int, none_type): Specifies the number of directories at a specific time.. [optional]  # noqa: E501
            num_files (int, none_type): Specifies the number of files.. [optional]  # noqa: E501
            num_files_prev (int, none_type): Specifies the number of files at a specific time.. [optional]  # noqa: E501
            protected_views (int, none_type): Specifies the number of all protected views.. [optional]  # noqa: E501
            replicated_in_views (int, none_type): Specifies the number of all the views that are replicated from remote clusters.. [optional]  # noqa: E501
            replicated_out_views (int, none_type): Specifies the number of all the views that are replicated out to remote clusters.. [optional]  # noqa: E501
            storage_consumed_bytes (int, none_type): Specifies the storage consumed of all the views in bytes.. [optional]  # noqa: E501
            storage_consumed_bytes_prev (int, none_type): Specifies the storage consumed by all the views in bytes at a specific time.. [optional]  # noqa: E501
            storage_consumed_bytes_prev_timestamp_usec (int, none_type): Specifies the timestamp in micro seconds when 'storageConsumedBytesPrev' was calculated.. [optional]  # noqa: E501
            storage_consumed_bytes_timestamp_usec (int, none_type): Specifies the timestamp in micro seconds when 'storageConsumedBytes' was calculated.. [optional]  # noqa: E501
            total_views (int, none_type): Specifies the number of all the views.. [optional]  # noqa: E501
            view_entity_id (str, none_type): Specifies the entity id of all the views.. [optional]  # noqa: E501
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


