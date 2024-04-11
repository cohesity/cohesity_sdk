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
    from cohesity_sdk.helios.model.common_idp_params import CommonIdpParams
    globals()['CommonIdpParams'] = CommonIdpParams


class CreateOrUpdateIdpRequest(ModelComposed):
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
        lazy_import()
        return {
            'name': (str, none_type,),  # noqa: E501
            'domain': (str, none_type,),  # noqa: E501
            'sso_url': (str, none_type,),  # noqa: E501
            'issuer_id': (str, none_type,),  # noqa: E501
            'certificate': (str, none_type,),  # noqa: E501
            'sf_account_id': (str, none_type,),  # noqa: E501
            'default_roles': ([str], none_type,),  # noqa: E501
            'default_clusters': ([str], none_type,),  # noqa: E501
            'sign_request': (bool, none_type,),  # noqa: E501
            'is_enabled': (bool, none_type,),  # noqa: E501
            'tenant_id': (str, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None



    attribute_map = {
        'name': 'name',  # noqa: E501
        'domain': 'domain',  # noqa: E501
        'sso_url': 'ssoUrl',  # noqa: E501
        'issuer_id': 'issuerId',  # noqa: E501
        'certificate': 'certificate',  # noqa: E501
        'sf_account_id': 'sfAccountId',  # noqa: E501
        'default_roles': 'defaultRoles',  # noqa: E501
        'default_clusters': 'defaultClusters',  # noqa: E501
        'sign_request': 'signRequest',  # noqa: E501
        'is_enabled': 'isEnabled',  # noqa: E501
        'tenant_id': 'tenantId',  # noqa: E501
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
    def __init__(self, name, domain, sso_url, issuer_id, certificate, *args, **kwargs):  # noqa: E501
        """CreateOrUpdateIdpRequest - a model defined in OpenAPI

        Args:
            name (str, none_type): Specifies the name of the vendor providing IDP service.
            domain (str, none_type): Specifies a unique name for this IdP configuration.
            sso_url (str, none_type): Specifies the SSO URL of the IdP service for the customer. This is the URL given by IdP when the customer created an account. For example, dev-332534.oktapreview.com.
            issuer_id (str, none_type): Specifies the IdP provided Issuer ID for the app. For example, exkh1aov1nhHrgFhN0h7.
            certificate (str, none_type): Specifies the certificate generated for the app by the IdP service when the Helios is registered as an app. This is required to verify the SAML response.

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

            sf_account_id (str, none_type): Specifies the salesforce account ID linked to this IDP. Either of TenantId or SfAccountId would be set for IdP.. [optional]  # noqa: E501
            default_roles ([str], none_type): Specifies a list of default roles assigned to an IdP user if rolesSamlAttributeName is not given.. [optional]  # noqa: E501
            default_clusters ([str], none_type): Specifies a list of default clusterIds assigned to an IdP user if clustersSamlAttributeName is not given. 'All' must be specified to give access to all clusters.. [optional]  # noqa: E501
            sign_request (bool, none_type): Specifies whether to sign the SAML request or not. When it is set to true, SAML request will be signed. When it is set to false, SAML request is not signed. Default is false. Set this flag to true if the IdP site is configured to expect the SAML request from Helios signed. If this is set to true, users must get the Helios certificate and upload it on the IdP site.. [optional]  # noqa: E501
            is_enabled (bool, none_type): Specifies a flag to enable or disable this IdP service. When it is set to true, IdP service is enabled. When it is set to false, IdP service is disabled. Default value is true.. [optional]  # noqa: E501
            tenant_id (str, none_type): Specifies the Tenant Id if the IdP is configured for a Tenant. Either of TenantId or SfAccountId would be set for IdP.. [optional]  # noqa: E501
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
            'name': name,
            'domain': domain,
            'sso_url': sso_url,
            'issuer_id': issuer_id,
            'certificate': certificate,
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
              CommonIdpParams,
          ],
          'oneOf': [
          ],
        }
