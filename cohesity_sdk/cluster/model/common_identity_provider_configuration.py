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


class CommonIdentityProviderConfiguration(ModelNormal):
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

    allowed_values = {}

    validations = {}

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
            "certificate": (
                str,
                none_type,
            ),  # noqa: E501
            "issuer_id": (
                str,
                none_type,
            ),  # noqa: E501
            "sso_url": (
                str,
                none_type,
            ),  # noqa: E501
            "allow_local_user_login": (
                bool,
                none_type,
            ),  # noqa: E501
            "certificate_filename": (
                str,
                none_type,
            ),  # noqa: E501
            "is_enabled": (
                bool,
                none_type,
            ),  # noqa: E501
            "roles": (
                [str],
                none_type,
            ),  # noqa: E501
            "saml_attribute_name": (
                str,
                none_type,
            ),  # noqa: E501
            "sign_request": (
                bool,
                none_type,
            ),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None

    attribute_map = {
        "certificate": "certificate",  # noqa: E501
        "issuer_id": "issuerId",  # noqa: E501
        "sso_url": "ssoUrl",  # noqa: E501
        "allow_local_user_login": "allowLocalUserLogin",  # noqa: E501
        "certificate_filename": "certificateFilename",  # noqa: E501
        "is_enabled": "isEnabled",  # noqa: E501
        "roles": "roles",  # noqa: E501
        "saml_attribute_name": "samlAttributeName",  # noqa: E501
        "sign_request": "signRequest",  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set(
        [
            "_data_store",
            "_check_type",
            "_spec_property_naming",
            "_path_to_item",
            "_configuration",
            "_visited_composed_classes",
        ]
    )

    @convert_js_args_to_python_args
    def __init__(self, certificate, issuer_id, sso_url, *args, **kwargs):  # noqa: E501
        """CommonIdentityProviderConfiguration - a model defined in OpenAPI

        Args:
            certificate (str, none_type): Specifies the certificate generated for the app by the idp service when the cluster is registered as an app. This is required to verify the SAML response.
            issuer_id (str, none_type): Specifies identity provider issuer id
            sso_url (str, none_type): Specifies the identity provider SSO url

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

            allow_local_user_login (bool, none_type): Specifies if local user login is allowed. When idp is configured, only idp users are allowed to login to the cluster, local login is disabled except for users with admin role. If this flag is set to true, local (non-idp) logins are allowed for all local and AD users. Local or AD users with admin role can login always independent of this flag's setting. By default there is no local authentication i.e the value is false.. [optional]  # noqa: E501
            certificate_filename (str, none_type): Specifies the filename used for the certificate. The default value is idp_certificate.pem. [optional]  # noqa: E501
            is_enabled (bool, none_type): Specifies a flag to enable or disable this idp service. When it is set to true, idp service is enabled. When it is set to false, idp service is disabled. By defaut idp is enabled i.e the value is true.. [optional]  # noqa: E501
            roles ([str], none_type): Specifies the default roles assined for all SSO users. [optional]  # noqa: E501
            saml_attribute_name (str, none_type): Specifies the SAML attribute name that contains a comma separated list of cluster roles. This sets the default roles for all SSO users. Either this field or roles must be set, this field takes higher precedence than the roles field.. [optional]  # noqa: E501
            sign_request (bool, none_type): Specifies whether to sign the SAML request or not. When it is set to true, SAML request will be signed. When it is set to false, SAML request is not signed. Default is false, set this flag to true if the idp site is configured to expect the SAML request from the Cluster signed. If this is set to true, users must get the cluster's certificate and upload it on the idp site.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop("_check_type", True)
        _spec_property_naming = kwargs.pop("_spec_property_naming", False)
        _path_to_item = kwargs.pop("_path_to_item", ())
        _configuration = kwargs.pop("_configuration", None)
        _visited_composed_classes = kwargs.pop("_visited_composed_classes", ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments."
                % (
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

        self.certificate = certificate
        self.issuer_id = issuer_id
        self.sso_url = sso_url
        for var_name, var_value in kwargs.items():
            if (
                var_name not in self.attribute_map
                and self._configuration is not None
                and self._configuration.discard_unknown_keys
                and self.additional_properties_type is None
            ):
                # discard variable.
                continue
            setattr(self, var_name, var_value)
