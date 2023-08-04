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
    from cohesity_sdk.cluster.model.object_protection_group_summary import ObjectProtectionGroupSummary
    from cohesity_sdk.cluster.model.protection_summary import ProtectionSummary
    globals()['ObjectProtectionGroupSummary'] = ObjectProtectionGroupSummary
    globals()['ProtectionSummary'] = ProtectionSummary


class ObjectProtectionInfo(ModelNormal):
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
        ('last_run_status',): {
            'None': None,
            'ACCEPTED': "Accepted",
            'RUNNING': "Running",
            'CANCELED': "Canceled",
            'CANCELING': "Canceling",
            'FAILED': "Failed",
            'MISSED': "Missed",
            'SUCCEEDED': "Succeeded",
            'SUCCEEDEDWITHWARNING': "SucceededWithWarning",
            'ONHOLD': "OnHold",
            'FINALIZING': "Finalizing",
            'SKIPPED': "Skipped",
            'PAUSED': "Paused",
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
            'object_id': (int, none_type,),  # noqa: E501
            'source_id': (int, none_type,),  # noqa: E501
            'view_id': (int, none_type,),  # noqa: E501
            'region_id': (str, none_type,),  # noqa: E501
            'cluster_id': (int, none_type,),  # noqa: E501
            'cluster_incarnation_id': (int, none_type,),  # noqa: E501
            'tenant_ids': ([str],),  # noqa: E501
            'is_deleted': (bool, none_type,),  # noqa: E501
            'protection_groups': ([ObjectProtectionGroupSummary], none_type,),  # noqa: E501
            'object_backup_configuration': ([ProtectionSummary], none_type,),  # noqa: E501
            'last_run_status': (str, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None



    attribute_map = {
        'object_id': 'objectId',  # noqa: E501
        'source_id': 'sourceId',  # noqa: E501
        'view_id': 'viewId',  # noqa: E501
        'region_id': 'regionId',  # noqa: E501
        'cluster_id': 'clusterId',  # noqa: E501
        'cluster_incarnation_id': 'clusterIncarnationId',  # noqa: E501
        'tenant_ids': 'tenantIds',  # noqa: E501
        'is_deleted': 'isDeleted',  # noqa: E501
        'protection_groups': 'protectionGroups',  # noqa: E501
        'object_backup_configuration': 'objectBackupConfiguration',  # noqa: E501
        'last_run_status': 'lastRunStatus',  # noqa: E501
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
        """ObjectProtectionInfo - a model defined in OpenAPI

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

            object_id (int, none_type): Specifies the object id.. [optional]  # noqa: E501
            source_id (int, none_type): Specifies the source id.. [optional]  # noqa: E501
            view_id (int, none_type): Specifies the view id for the object.. [optional]  # noqa: E501
            region_id (str, none_type): Specifies the region id where this object belongs to.. [optional]  # noqa: E501
            cluster_id (int, none_type): Specifies the cluster id where this object belongs to.. [optional]  # noqa: E501
            cluster_incarnation_id (int, none_type): Specifies the cluster incarnation id where this object belongs to.. [optional]  # noqa: E501
            tenant_ids ([str]): List of Tenants the object belongs to.. [optional]  # noqa: E501
            is_deleted (bool, none_type): Specifies whether the object is deleted. Deleted objects can't be protected but can be recovered or unprotected.. [optional]  # noqa: E501
            protection_groups ([ObjectProtectionGroupSummary], none_type): Specifies a list of protection groups protecting this object.. [optional]  # noqa: E501
            object_backup_configuration ([ProtectionSummary], none_type): Specifies a list of object protections.. [optional]  # noqa: E501
            last_run_status (str, none_type): Specifies the status of the object's last protection run.. [optional]  # noqa: E501
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


