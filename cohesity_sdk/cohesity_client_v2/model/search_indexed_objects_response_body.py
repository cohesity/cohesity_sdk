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
    from cohesity_sdk.cohesity_client_v2.model.cassandra_indexed_object import CassandraIndexedObject
    from cohesity_sdk.cohesity_client_v2.model.common_search_indexed_objects_response_params import CommonSearchIndexedObjectsResponseParams
    from cohesity_sdk.cohesity_client_v2.model.couchbase_indexed_object import CouchbaseIndexedObject
    from cohesity_sdk.cohesity_client_v2.model.email import Email
    from cohesity_sdk.cohesity_client_v2.model.exchange_indexed_object import ExchangeIndexedObject
    from cohesity_sdk.cohesity_client_v2.model.file import File
    from cohesity_sdk.cohesity_client_v2.model.hbase_indexed_object import HbaseIndexedObject
    from cohesity_sdk.cohesity_client_v2.model.hdfs_indexed_object import HDFSIndexedObject
    from cohesity_sdk.cohesity_client_v2.model.hive_indexed_object import HiveIndexedObject
    from cohesity_sdk.cohesity_client_v2.model.mongo_indexed_object import MongoIndexedObject
    from cohesity_sdk.cohesity_client_v2.model.public_folder_item import PublicFolderItem
    from cohesity_sdk.cohesity_client_v2.model.search_indexed_objects_response_body_all_of import SearchIndexedObjectsResponseBodyAllOf
    globals()['CassandraIndexedObject'] = CassandraIndexedObject
    globals()['CommonSearchIndexedObjectsResponseParams'] = CommonSearchIndexedObjectsResponseParams
    globals()['CouchbaseIndexedObject'] = CouchbaseIndexedObject
    globals()['Email'] = Email
    globals()['ExchangeIndexedObject'] = ExchangeIndexedObject
    globals()['File'] = File
    globals()['HDFSIndexedObject'] = HDFSIndexedObject
    globals()['HbaseIndexedObject'] = HbaseIndexedObject
    globals()['HiveIndexedObject'] = HiveIndexedObject
    globals()['MongoIndexedObject'] = MongoIndexedObject
    globals()['PublicFolderItem'] = PublicFolderItem
    globals()['SearchIndexedObjectsResponseBodyAllOf'] = SearchIndexedObjectsResponseBodyAllOf


class SearchIndexedObjectsResponseBody(ModelComposed):
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
        ('object_type',): {
            'EMAILS': "Emails",
            'FILES': "Files",
            'CASSANDRAOBJECTS': "CassandraObjects",
            'COUCHBASEOBJECTS': "CouchbaseObjects",
            'HBASEOBJECTS': "HbaseObjects",
            'HIVEOBJECTS': "HiveObjects",
            'MONGOOBJECTS': "MongoObjects",
            'HDFSOBJECTS': "HDFSObjects",
            'EXCHANGEOBJECTS': "ExchangeObjects",
            'PUBLICFOLDERS': "PublicFolders",
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
            'object_type': (str,),  # noqa: E501
            'count': (int, none_type,),  # noqa: E501
            'pagination_cookie': (str, none_type,),  # noqa: E501
            'emails': ([Email], none_type,),  # noqa: E501
            'files': ([File], none_type,),  # noqa: E501
            'cassandra_objects': ([CassandraIndexedObject], none_type,),  # noqa: E501
            'couchbase_objects': ([CouchbaseIndexedObject], none_type,),  # noqa: E501
            'hbase_objects': ([HbaseIndexedObject], none_type,),  # noqa: E501
            'hive_objects': ([HiveIndexedObject], none_type,),  # noqa: E501
            'mongo_objects': ([MongoIndexedObject], none_type,),  # noqa: E501
            'hdfs_objects': ([HDFSIndexedObject], none_type,),  # noqa: E501
            'exchange_objects': ([ExchangeIndexedObject], none_type,),  # noqa: E501
            'public_folder_items': ([PublicFolderItem], none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None



    attribute_map = {
        'object_type': 'objectType',  # noqa: E501
        'count': 'count',  # noqa: E501
        'pagination_cookie': 'paginationCookie',  # noqa: E501
        'emails': 'emails',  # noqa: E501
        'files': 'files',  # noqa: E501
        'cassandra_objects': 'cassandraObjects',  # noqa: E501
        'couchbase_objects': 'couchbaseObjects',  # noqa: E501
        'hbase_objects': 'hbaseObjects',  # noqa: E501
        'hive_objects': 'hiveObjects',  # noqa: E501
        'mongo_objects': 'mongoObjects',  # noqa: E501
        'hdfs_objects': 'hdfsObjects',  # noqa: E501
        'exchange_objects': 'exchangeObjects',  # noqa: E501
        'public_folder_items': 'publicFolderItems',  # noqa: E501
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
    def __init__(self, *args, **kwargs):  # noqa: E501
        """SearchIndexedObjectsResponseBody - a model defined in OpenAPI

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

            object_type (str): Specifies the object type.. [optional]  # noqa: E501
            count (int, none_type): Specifies the total number of indexed objects that match the filter and search criteria. Use this value to determine how many additional requests are required to get the full result.. [optional]  # noqa: E501
            pagination_cookie (str, none_type): Specifies cookie for resuming search if pagination is being used.. [optional]  # noqa: E501
            emails ([Email], none_type): Specifies the indexed emails and email folders.. [optional]  # noqa: E501
            files ([File], none_type): Specifies the indexed files and file folders.. [optional]  # noqa: E501
            cassandra_objects ([CassandraIndexedObject], none_type): Specifies the indexed Cassandra objects.. [optional]  # noqa: E501
            couchbase_objects ([CouchbaseIndexedObject], none_type): Specifies the indexed Couchbase objects.. [optional]  # noqa: E501
            hbase_objects ([HbaseIndexedObject], none_type): Specifies the indexed Hbase objects.. [optional]  # noqa: E501
            hive_objects ([HiveIndexedObject], none_type): Specifies the indexed Hive objects.. [optional]  # noqa: E501
            mongo_objects ([MongoIndexedObject], none_type): Specifies the indexed Mongo objects.. [optional]  # noqa: E501
            hdfs_objects ([HDFSIndexedObject], none_type): Specifies the indexed HDFS objects.. [optional]  # noqa: E501
            exchange_objects ([ExchangeIndexedObject], none_type): Specifies the indexed HDFS objects.. [optional]  # noqa: E501
            public_folder_items ([PublicFolderItem], none_type): Specifies the indexed Public folder items.. [optional]  # noqa: E501
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
              CommonSearchIndexedObjectsResponseParams,
              SearchIndexedObjectsResponseBodyAllOf,
          ],
          'oneOf': [
          ],
        }

