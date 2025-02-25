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
    from cohesity_sdk.cluster.model.create_cluster_vlan_params_all_of import (
        CreateClusterVlanParamsAllOf,
    )
    from cohesity_sdk.cluster.model.dns_delegation_zone import DnsDelegationZone
    from cohesity_sdk.cluster.model.ip_pool import IpPool
    from cohesity_sdk.cluster.model.ip_range import IpRange
    from cohesity_sdk.cluster.model.update_cluster_vlan_params import (
        UpdateClusterVlanParams,
    )

    globals()["CreateClusterVlanParamsAllOf"] = CreateClusterVlanParamsAllOf
    globals()["DnsDelegationZone"] = DnsDelegationZone
    globals()["IpPool"] = IpPool
    globals()["IpRange"] = IpRange
    globals()["UpdateClusterVlanParams"] = UpdateClusterVlanParams


class CreateClusterVlanParams(ModelComposed):
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
        ("ip_addresses_type",): {
            "None": None,
            "IPV4": "Ipv4",
            "IPV6": "Ipv6",
        },
    }

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
        lazy_import()
        return {
            "interface_name": (str,),  # noqa: E501
            "all_tenant_access": (
                bool,
                none_type,
            ),  # noqa: E501
            "app_ips": (
                [str],
                none_type,
            ),  # noqa: E501
            "description": (
                str,
                none_type,
            ),  # noqa: E501
            "dns_delegation_zones": (
                [DnsDelegationZone],
                none_type,
            ),  # noqa: E501
            "ecmp_enabled": (
                bool,
                none_type,
            ),  # noqa: E501
            "fqdn": (
                str,
                none_type,
            ),  # noqa: E501
            "gateway": (
                str,
                none_type,
            ),  # noqa: E501
            "ip_addresses_type": (
                str,
                none_type,
            ),  # noqa: E501
            "ip_pools": (
                [IpPool],
                none_type,
            ),  # noqa: E501
            "ip_ranges": (
                [IpRange],
                none_type,
            ),  # noqa: E501
            "ips": (
                [str],
                none_type,
            ),  # noqa: E501
            "mtu": (
                int,
                none_type,
            ),  # noqa: E501
            "subnet": (
                str,
                none_type,
            ),  # noqa: E501
            "tenant_id": (
                str,
                none_type,
            ),  # noqa: E501
            "vlan_name": (
                str,
                none_type,
            ),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None

    attribute_map = {
        "interface_name": "interfaceName",  # noqa: E501
        "all_tenant_access": "allTenantAccess",  # noqa: E501
        "app_ips": "appIps",  # noqa: E501
        "description": "description",  # noqa: E501
        "dns_delegation_zones": "dnsDelegationZones",  # noqa: E501
        "ecmp_enabled": "ecmpEnabled",  # noqa: E501
        "fqdn": "fqdn",  # noqa: E501
        "gateway": "gateway",  # noqa: E501
        "ip_addresses_type": "ipAddressesType",  # noqa: E501
        "ip_pools": "ipPools",  # noqa: E501
        "ip_ranges": "ipRanges",  # noqa: E501
        "ips": "ips",  # noqa: E501
        "mtu": "mtu",  # noqa: E501
        "subnet": "subnet",  # noqa: E501
        "tenant_id": "tenantId",  # noqa: E501
        "vlan_name": "vlanName",  # noqa: E501
    }

    required_properties = set(
        [
            "_data_store",
            "_check_type",
            "_spec_property_naming",
            "_path_to_item",
            "_configuration",
            "_visited_composed_classes",
            "_composed_instances",
            "_var_name_to_model_instances",
            "_additional_properties_model_instances",
        ]
    )

    @convert_js_args_to_python_args
    def __init__(self, interface_name, *args, **kwargs):  # noqa: E501
        """CreateClusterVlanParams - a model defined in OpenAPI

        Args:
            interface_name (str): Vlan interface name, it should be in interface_group_name.vlan_id format.

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

            all_tenant_access (bool, none_type): Allow vlan to be used by all tenants without explicit assignment. Set to true only when the vlan is not assigned to any tenant.. [optional] if omitted the server will use the default value of False  # noqa: E501
            app_ips ([str], none_type): Vlan IP addresses for apps.. [optional]  # noqa: E501
            description (str, none_type): Description of the vlan.. [optional]  # noqa: E501
            dns_delegation_zones ([DnsDelegationZone], none_type): DNS delegation zones of the vlan.. [optional]  # noqa: E501
            ecmp_enabled (bool, none_type): Set to true to enable ECMP in the vlan.. [optional] if omitted the server will use the default value of False  # noqa: E501
            fqdn (str, none_type): FQDN of the vlan.. [optional]  # noqa: E501
            gateway (str, none_type): Subnet gateway of the vlan. This can be Ipv4 or Ipv6 gateway based on the IP addresses type.. [optional]  # noqa: E501
            ip_addresses_type (str, none_type): Type of IP addresses. The default value is Ipv4.. [optional]  # noqa: E501
            ip_pools ([IpPool], none_type): IP pools from the vlan ip addresses, the IPs in a pool goes together. One IP from each pool forms a VIP group.. [optional]  # noqa: E501
            ip_ranges ([IpRange], none_type): Vlan IP address ranges, only one of ips or ipRanges parameters should be given.. [optional]  # noqa: E501
            ips ([str], none_type): Vlan IP addresses, only one of ips or ipRanges parameters should be given.. [optional]  # noqa: E501
            mtu (int, none_type): MTU of the vlan.. [optional]  # noqa: E501
            subnet (str, none_type): IPv6 or IPv6 subnet in CIDR format i.e ip-address/prefix. Examples: IPv4 subnet'192.168.0.101/24', '10.10.1.32/27'. IPv6 subnet '3005:1231:2006:0025::0/96', 3005:1231:2006:0025::0/128. [optional]  # noqa: E501
            tenant_id (str, none_type): Tenant id to assign vlan to a tenant.. [optional]  # noqa: E501
            vlan_name (str, none_type): Name of the Vlan.. [optional]  # noqa: E501
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

        constant_args = {
            "_check_type": _check_type,
            "_path_to_item": _path_to_item,
            "_spec_property_naming": _spec_property_naming,
            "_configuration": _configuration,
            "_visited_composed_classes": self._visited_composed_classes,
        }
        required_args = {
            "interface_name": interface_name,
        }
        model_args = {}
        model_args.update(required_args)
        model_args.update(kwargs)
        composed_info = validate_get_composed_info(constant_args, model_args, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        unused_args = composed_info[3]

        for var_name, var_value in required_args.items():
            setattr(self, var_name, var_value)
        for var_name, var_value in kwargs.items():
            if (
                var_name in unused_args
                and self._configuration is not None
                and self._configuration.discard_unknown_keys
                and not self._additional_properties_model_instances
            ):
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
            "anyOf": [],
            "allOf": [
                CreateClusterVlanParamsAllOf,
                UpdateClusterVlanParams,
            ],
            "oneOf": [],
        }
