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
    from cohesity_sdk.cluster.model.azure_application_credentials import AzureApplicationCredentials
    from cohesity_sdk.cluster.model.azure_subscription import AzureSubscription
    globals()['AzureApplicationCredentials'] = AzureApplicationCredentials
    globals()['AzureSubscription'] = AzureSubscription


class AzureSourceRegistrationParams(ModelNormal):
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
        ('registration_level',): {
            'None': None,
            'KTENANT': "kTenant",
            'KSUBSCRIPTION': "kSubscription",
        },
        ('registration_workflow',): {
            'None': None,
            'KEXPRESS': "kExpress",
            'KMANUAL': "kManual",
        },
        ('use_cases',): {
            'None': None,
            'KVIRTUALMACHINE': "kVirtualMachine",
            'KSQL': "kSQL",
        },
    }

    validations = {
        ('subscription_details',): {
            'min_items': 1,
        },

        ('use_cases',): {
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
            'registration_level': (str, none_type,),  # noqa: E501
            'registration_workflow': (str, none_type,),  # noqa: E501
            'application_credentials': ([AzureApplicationCredentials],),  # noqa: E501
            'azure_tenant_id': (str, none_type,),  # noqa: E501
            'subscription_details': ([AzureSubscription],),  # noqa: E501
            'use_cases': ([str], none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None



    attribute_map = {
        'registration_level': 'registrationLevel',  # noqa: E501
        'registration_workflow': 'registrationWorkflow',  # noqa: E501
        'application_credentials': 'applicationCredentials',  # noqa: E501
        'azure_tenant_id': 'azureTenantId',  # noqa: E501
        'subscription_details': 'subscriptionDetails',  # noqa: E501
        'use_cases': 'useCases',  # noqa: E501
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
    def __init__(self, registration_level, registration_workflow, *args, **kwargs):  # noqa: E501
        """AzureSourceRegistrationParams - a model defined in OpenAPI

        Args:
            registration_level (str, none_type): Specifies whether the registration is at tenant level or subscription level.
            registration_workflow (str, none_type): Specifies whether the type of registration is express or manual.

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

            application_credentials ([AzureApplicationCredentials]): Specifies the credentials for a list of applications from azure active directory.. [optional]  # noqa: E501
            azure_tenant_id (str, none_type): Specifies Tenant Id of the active directory of Azure account. Accpets both Azure tanant Id and tenant domain name.. [optional]  # noqa: E501
            subscription_details ([AzureSubscription]): Specifies the list subscription ids to be registered.. [optional]  # noqa: E501
            use_cases ([str], none_type): The use cases for which the source is to be registered.. [optional]  # noqa: E501
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


        self.registration_level = registration_level
        self.registration_workflow = registration_workflow
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)


