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
    from cohesity_sdk.cluster.model.kubernetes_filter_params import KubernetesFilterParams
    from cohesity_sdk.cluster.model.kubernetes_protection_group_object_params import KubernetesProtectionGroupObjectParams
    globals()['KubernetesFilterParams'] = KubernetesFilterParams
    globals()['KubernetesProtectionGroupObjectParams'] = KubernetesProtectionGroupObjectParams


class KubernetesProtectionGroupParams(ModelNormal):
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
        ('exclude_object_ids',): {
        },

        ('objects',): {
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
            'exclude_label_ids': ([[int]],),  # noqa: E501
            'exclude_object_ids': ([int],),  # noqa: E501
            'exclude_params': (KubernetesFilterParams,),  # noqa: E501
            'include_params': (KubernetesFilterParams,),  # noqa: E501
            'label_ids': ([[int]], none_type,),  # noqa: E501
            'leverage_csi_snapshot': (bool, none_type,),  # noqa: E501
            'objects': ([KubernetesProtectionGroupObjectParams],),  # noqa: E501
            'source_id': (int, none_type,),  # noqa: E501
            'source_name': (str, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None



    attribute_map = {
        'exclude_label_ids': 'excludeLabelIds',  # noqa: E501
        'exclude_object_ids': 'excludeObjectIds',  # noqa: E501
        'exclude_params': 'excludeParams',  # noqa: E501
        'include_params': 'includeParams',  # noqa: E501
        'label_ids': 'labelIds',  # noqa: E501
        'leverage_csi_snapshot': 'leverageCSISnapshot',  # noqa: E501
        'objects': 'objects',  # noqa: E501
        'source_id': 'sourceId',  # noqa: E501
        'source_name': 'sourceName',  # noqa: E501
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
        """KubernetesProtectionGroupParams - a model defined in OpenAPI

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

            exclude_label_ids ([[int]]): Array of arrays of label IDs that specify labels to exclude. Optionally specify a list of labels to exclude from protecting by listing protection source ids of labels in this two dimensional array. Using this two dimensional array of label IDs, the Cluster generates a list of namespaces to exclude from protecting, which are derived from intersections of the inner arrays and union of the outer array.. [optional]  # noqa: E501
            exclude_object_ids ([int]): Specifies the objects to be excluded in the Protection Group.. [optional]  # noqa: E501
            exclude_params (KubernetesFilterParams): [optional]  # noqa: E501
            include_params (KubernetesFilterParams): [optional]  # noqa: E501
            label_ids ([[int]], none_type): Array of array of label IDs that specify labels to protect. Optionally specify a list of labels to protect by listing protection source ids of labels in this two dimensional array. Using this two dimensional array of label IDs, the cluster generates a list of namespaces to protect, which are derived from intersections of the inner arrays and union of the outer array.. [optional]  # noqa: E501
            leverage_csi_snapshot (bool, none_type): Specifies if CSI snapshots should be used for backup of namespaces.. [optional]  # noqa: E501
            objects ([KubernetesProtectionGroupObjectParams]): Specifies the objects included in the Protection Group.. [optional]  # noqa: E501
            source_id (int, none_type): Specifies the id of the parent of the objects.. [optional]  # noqa: E501
            source_name (str, none_type): Specifies the name of the parent of the objects.. [optional]  # noqa: E501
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


