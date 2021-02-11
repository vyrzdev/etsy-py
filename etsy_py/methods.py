from .rq import RequiresOauth


# These methods are all auto-generated from the Etsy Method Table, by method_generator.py periodically
# Any manual changes will be overwritten!

# StartMethod: getMethodTable
# uri_parameters: 
# http_method: GET
def getMethodTable(self, query_params=None):
    return self.requester.make_request(
        uri="/",
        uri_params=[],
        method="GET",
        query_params=query_params
    )
# EndMethod: getMethodTable


# StartMethod: getPublicBaseline
# uri_parameters: 
# http_method: GET
def getPublicBaseline(self, query_params=None):
    return self.requester.make_request(
        uri="/baseline",
        uri_params=[],
        method="GET",
        query_params=query_params
    )
# EndMethod: getPublicBaseline


# StartMethod: findAllCountry
# uri_parameters: 
# http_method: GET
def findAllCountry(self, query_params=None):
    return self.requester.make_request(
        uri="/countries",
        uri_params=[],
        method="GET",
        query_params=query_params
    )
# EndMethod: findAllCountry


# StartMethod: getCountry
# uri_parameters: country_id
# http_method: GET
def getCountry(self, country_id, query_params=None):
    return self.requester.make_request(
        uri="/countries/:country_id",
        uri_params=[country_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: getCountry


# StartMethod: findByIsoCode
# uri_parameters: iso_code
# http_method: GET
def findByIsoCode(self, iso_code, query_params=None):
    return self.requester.make_request(
        uri="/countries/iso/:iso_code",
        uri_params=[iso_code],
        method="GET",
        query_params=query_params
    )
# EndMethod: findByIsoCode


# StartMethod: findAllFeaturedTreasuries
# uri_parameters: 
# http_method: GET
def findAllFeaturedTreasuries(self, query_params=None):
    return self.requester.make_request(
        uri="/featured_treasuries",
        uri_params=[],
        method="GET",
        query_params=query_params
    )
# EndMethod: findAllFeaturedTreasuries


# StartMethod: getFeaturedTreasuryById
# uri_parameters: featured_treasury_id
# http_method: GET
def getFeaturedTreasuryById(self, featured_treasury_id, query_params=None):
    return self.requester.make_request(
        uri="/featured_treasuries/:featured_treasury_id",
        uri_params=[featured_treasury_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: getFeaturedTreasuryById


# StartMethod: findAllListingsForFeaturedTreasuryId
# uri_parameters: featured_treasury_id
# http_method: GET
def findAllListingsForFeaturedTreasuryId(self, featured_treasury_id, query_params=None):
    return self.requester.make_request(
        uri="/featured_treasuries/:featured_treasury_id/listings",
        uri_params=[featured_treasury_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: findAllListingsForFeaturedTreasuryId


# StartMethod: findAllActiveListingsForFeaturedTreasuryId
# uri_parameters: featured_treasury_id
# http_method: GET
def findAllActiveListingsForFeaturedTreasuryId(self, featured_treasury_id, query_params=None):
    return self.requester.make_request(
        uri="/featured_treasuries/:featured_treasury_id/listings/active",
        uri_params=[featured_treasury_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: findAllActiveListingsForFeaturedTreasuryId


# StartMethod: findAllFeaturedListings
# uri_parameters: 
# http_method: GET
def findAllFeaturedListings(self, query_params=None):
    return self.requester.make_request(
        uri="/featured_treasuries/listings",
        uri_params=[],
        method="GET",
        query_params=query_params
    )
# EndMethod: findAllFeaturedListings


# StartMethod: findAllCurrentFeaturedListings
# uri_parameters: 
# http_method: GET
def findAllCurrentFeaturedListings(self, query_params=None):
    return self.requester.make_request(
        uri="/featured_treasuries/listings/homepage_current",
        uri_params=[],
        method="GET",
        query_params=query_params
    )
# EndMethod: findAllCurrentFeaturedListings


# StartMethod: findAllFeaturedTreasuriesByOwner
# uri_parameters: owner_id
# http_method: GET
def findAllFeaturedTreasuriesByOwner(self, owner_id, query_params=None):
    return self.requester.make_request(
        uri="/featured_treasuries/owner/:owner_id",
        uri_params=[owner_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: findAllFeaturedTreasuriesByOwner


# StartMethod: getGuest
# uri_parameters: guest_id
# http_method: GET
def getGuest(self, guest_id, query_params=None):
    return self.requester.make_request(
        uri="/guests/:guest_id",
        uri_params=[guest_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: getGuest


# StartMethod: findAllGuestCarts
# uri_parameters: guest_id
# http_method: GET
def findAllGuestCarts(self, guest_id, query_params=None):
    return self.requester.make_request(
        uri="/guests/:guest_id/carts",
        uri_params=[guest_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: findAllGuestCarts


# StartMethod: addToGuestCart
# uri_parameters: guest_id
# http_method: POST
def addToGuestCart(self, guest_id, query_params=None, data=None):
    return self.requester.make_request(
        uri="/guests/:guest_id/carts",
        uri_params=[guest_id],
        method="POST",
        query_params=query_params
    )
# EndMethod: addToGuestCart


# StartMethod: updateGuestCartListingQuantity
# uri_parameters: guest_id
# http_method: PUT
def updateGuestCartListingQuantity(self, guest_id, query_params=None, data=None):
    return self.requester.make_request(
        uri="/guests/:guest_id/carts",
        uri_params=[guest_id],
        method="PUT",
        query_params=query_params
    )
# EndMethod: updateGuestCartListingQuantity


# StartMethod: removeGuestCartListing
# uri_parameters: guest_id
# http_method: DELETE
def removeGuestCartListing(self, guest_id, query_params=None):
    return self.requester.make_request(
        uri="/guests/:guest_id/carts",
        uri_params=[guest_id],
        method="DELETE",
        query_params=query_params
    )
# EndMethod: removeGuestCartListing


# StartMethod: findGuestCart
# uri_parameters: guest_id|cart_id
# http_method: GET
def findGuestCart(self, guest_id, cart_id, query_params=None):
    return self.requester.make_request(
        uri="/guests/:guest_id/carts/:cart_id",
        uri_params=[guest_id, cart_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: findGuestCart


# StartMethod: updateGuestCart
# uri_parameters: guest_id|cart_id
# http_method: PUT
def updateGuestCart(self, guest_id, cart_id, query_params=None, data=None):
    return self.requester.make_request(
        uri="/guests/:guest_id/carts/:cart_id",
        uri_params=[guest_id, cart_id],
        method="PUT",
        query_params=query_params
    )
# EndMethod: updateGuestCart


# StartMethod: deleteGuestCart
# uri_parameters: guest_id|cart_id
# http_method: DELETE
def deleteGuestCart(self, guest_id, cart_id, query_params=None):
    return self.requester.make_request(
        uri="/guests/:guest_id/carts/:cart_id",
        uri_params=[guest_id, cart_id],
        method="DELETE",
        query_params=query_params
    )
# EndMethod: deleteGuestCart


# StartMethod: claimGuest
# uri_parameters: guest_id
# http_method: POST
def claimGuest(self, guest_id, query_params=None, data=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/guests/:guest_id/claim",
        uri_params=[guest_id],
        method="POST",
        query_params=query_params
    )
# EndMethod: claimGuest


# StartMethod: mergeGuest
# uri_parameters: guest_id
# http_method: POST
def mergeGuest(self, guest_id, query_params=None, data=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/guests/:guest_id/merge",
        uri_params=[guest_id],
        method="POST",
        query_params=query_params
    )
# EndMethod: mergeGuest


# StartMethod: generateGuest
# uri_parameters: 
# http_method: GET
def generateGuest(self, query_params=None):
    return self.requester.make_request(
        uri="/guests/generator",
        uri_params=[],
        method="GET",
        query_params=query_params
    )
# EndMethod: generateGuest


# StartMethod: listImageTypes
# uri_parameters: 
# http_method: GET
def listImageTypes(self, query_params=None):
    return self.requester.make_request(
        uri="/image_types",
        uri_params=[],
        method="GET",
        query_params=query_params
    )
# EndMethod: listImageTypes


# StartMethod: createListing
# uri_parameters: 
# http_method: POST
def createListing(self, query_params=None, data=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/listings",
        uri_params=[],
        method="POST",
        query_params=query_params
    )
# EndMethod: createListing


# StartMethod: getListing
# uri_parameters: listing_id
# http_method: GET
def getListing(self, listing_id, query_params=None):
    return self.requester.make_request(
        uri="/listings/:listing_id",
        uri_params=[listing_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: getListing


# StartMethod: updateListing
# uri_parameters: listing_id
# http_method: PUT
def updateListing(self, listing_id, query_params=None, data=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/listings/:listing_id",
        uri_params=[listing_id],
        method="PUT",
        query_params=query_params
    )
# EndMethod: updateListing


# StartMethod: deleteListing
# uri_parameters: listing_id
# http_method: DELETE
def deleteListing(self, listing_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/listings/:listing_id",
        uri_params=[listing_id],
        method="DELETE",
        query_params=query_params
    )
# EndMethod: deleteListing


# StartMethod: getAttributes
# uri_parameters: listing_id
# http_method: GET
def getAttributes(self, listing_id, query_params=None):
    return self.requester.make_request(
        uri="/listings/:listing_id/attributes",
        uri_params=[listing_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: getAttributes


# StartMethod: getAttribute
# uri_parameters: listing_id|property_id
# http_method: GET
def getAttribute(self, listing_id, property_id, query_params=None):
    return self.requester.make_request(
        uri="/listings/:listing_id/attributes/:property_id",
        uri_params=[listing_id, property_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: getAttribute


# StartMethod: updateAttribute
# uri_parameters: listing_id|property_id
# http_method: PUT
def updateAttribute(self, listing_id, property_id, query_params=None, data=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/listings/:listing_id/attributes/:property_id",
        uri_params=[listing_id, property_id],
        method="PUT",
        query_params=query_params
    )
# EndMethod: updateAttribute


# StartMethod: deleteAttribute
# uri_parameters: listing_id|property_id
# http_method: DELETE
def deleteAttribute(self, listing_id, property_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/listings/:listing_id/attributes/:property_id",
        uri_params=[listing_id, property_id],
        method="DELETE",
        query_params=query_params
    )
# EndMethod: deleteAttribute


# StartMethod: findAllListingFavoredBy
# uri_parameters: listing_id
# http_method: GET
def findAllListingFavoredBy(self, listing_id, query_params=None):
    return self.requester.make_request(
        uri="/listings/:listing_id/favored-by",
        uri_params=[listing_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: findAllListingFavoredBy


# StartMethod: findAllListingFiles
# uri_parameters: listing_id
# http_method: GET
def findAllListingFiles(self, listing_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/listings/:listing_id/files",
        uri_params=[listing_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: findAllListingFiles


# StartMethod: uploadListingFile
# uri_parameters: listing_id
# http_method: POST
def uploadListingFile(self, listing_id, query_params=None, data=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/listings/:listing_id/files",
        uri_params=[listing_id],
        method="POST",
        query_params=query_params
    )
# EndMethod: uploadListingFile


# StartMethod: findListingFile
# uri_parameters: listing_id|listing_file_id
# http_method: GET
def findListingFile(self, listing_id, listing_file_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/listings/:listing_id/files/:listing_file_id",
        uri_params=[listing_id, listing_file_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: findListingFile


# StartMethod: deleteListingFile
# uri_parameters: listing_id|listing_file_id
# http_method: DELETE
def deleteListingFile(self, listing_id, listing_file_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/listings/:listing_id/files/:listing_file_id",
        uri_params=[listing_id, listing_file_id],
        method="DELETE",
        query_params=query_params
    )
# EndMethod: deleteListingFile


# StartMethod: findAllListingImages
# uri_parameters: listing_id
# http_method: GET
def findAllListingImages(self, listing_id, query_params=None):
    return self.requester.make_request(
        uri="/listings/:listing_id/images",
        uri_params=[listing_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: findAllListingImages


# StartMethod: uploadListingImage
# uri_parameters: listing_id
# http_method: POST
def uploadListingImage(self, listing_id, query_params=None, data=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/listings/:listing_id/images",
        uri_params=[listing_id],
        method="POST",
        query_params=query_params
    )
# EndMethod: uploadListingImage


# StartMethod: getImage_Listing
# uri_parameters: listing_id|listing_image_id
# http_method: GET
def getImage_Listing(self, listing_id, listing_image_id, query_params=None):
    return self.requester.make_request(
        uri="/listings/:listing_id/images/:listing_image_id",
        uri_params=[listing_id, listing_image_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: getImage_Listing


# StartMethod: deleteListingImage
# uri_parameters: listing_id|listing_image_id
# http_method: DELETE
def deleteListingImage(self, listing_id, listing_image_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/listings/:listing_id/images/:listing_image_id",
        uri_params=[listing_id, listing_image_id],
        method="DELETE",
        query_params=query_params
    )
# EndMethod: deleteListingImage


# StartMethod: getInventory
# uri_parameters: listing_id
# http_method: GET
def getInventory(self, listing_id, query_params=None):
    return self.requester.make_request(
        uri="/listings/:listing_id/inventory",
        uri_params=[listing_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: getInventory


# StartMethod: updateInventory
# uri_parameters: listing_id
# http_method: PUT
def updateInventory(self, listing_id, query_params=None, data=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/listings/:listing_id/inventory",
        uri_params=[listing_id],
        method="PUT",
        query_params=query_params
    )
# EndMethod: updateInventory


# StartMethod: getProduct
# uri_parameters: listing_id|product_id
# http_method: GET
def getProduct(self, listing_id, product_id, query_params=None):
    return self.requester.make_request(
        uri="/listings/:listing_id/products/:product_id",
        uri_params=[listing_id, product_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: getProduct


# StartMethod: getOffering
# uri_parameters: listing_id|product_id|offering_id
# http_method: GET
def getOffering(self, listing_id, product_id, offering_id, query_params=None):
    return self.requester.make_request(
        uri="/listings/:listing_id/products/:product_id/offerings/:offering_id",
        uri_params=[listing_id, product_id, offering_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: getOffering


# StartMethod: findAllListingShippingProfileEntries
# uri_parameters: listing_id
# http_method: GET
def findAllListingShippingProfileEntries(self, listing_id, query_params=None):
    return self.requester.make_request(
        uri="/listings/:listing_id/shipping/info",
        uri_params=[listing_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: findAllListingShippingProfileEntries


# StartMethod: createShippingInfo
# uri_parameters: listing_id
# http_method: POST
def createShippingInfo(self, listing_id, query_params=None, data=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/listings/:listing_id/shipping/info",
        uri_params=[listing_id],
        method="POST",
        query_params=query_params
    )
# EndMethod: createShippingInfo


# StartMethod: getListingShippingUpgrades
# uri_parameters: listing_id
# http_method: GET
def getListingShippingUpgrades(self, listing_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/listings/:listing_id/shipping/upgrades",
        uri_params=[listing_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: getListingShippingUpgrades


# StartMethod: createListingShippingUpgrade
# uri_parameters: listing_id
# http_method: POST
def createListingShippingUpgrade(self, listing_id, query_params=None, data=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/listings/:listing_id/shipping/upgrades",
        uri_params=[listing_id],
        method="POST",
        query_params=query_params
    )
# EndMethod: createListingShippingUpgrade


# StartMethod: updateListingShippingUpgrade
# uri_parameters: listing_id
# http_method: PUT
def updateListingShippingUpgrade(self, listing_id, query_params=None, data=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/listings/:listing_id/shipping/upgrades",
        uri_params=[listing_id],
        method="PUT",
        query_params=query_params
    )
# EndMethod: updateListingShippingUpgrade


# StartMethod: deleteListingShippingUpgrade
# uri_parameters: listing_id
# http_method: DELETE
def deleteListingShippingUpgrade(self, listing_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/listings/:listing_id/shipping/upgrades",
        uri_params=[listing_id],
        method="DELETE",
        query_params=query_params
    )
# EndMethod: deleteListingShippingUpgrade


# StartMethod: findAllListingTransactions
# uri_parameters: listing_id
# http_method: GET
def findAllListingTransactions(self, listing_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/listings/:listing_id/transactions",
        uri_params=[listing_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: findAllListingTransactions


# StartMethod: getListingTranslation
# uri_parameters: listing_id|language
# http_method: GET
def getListingTranslation(self, listing_id, language, query_params=None):
    return self.requester.make_request(
        uri="/listings/:listing_id/translations/:language",
        uri_params=[listing_id, language],
        method="GET",
        query_params=query_params
    )
# EndMethod: getListingTranslation


# StartMethod: createListingTranslation
# uri_parameters: listing_id|language
# http_method: POST
def createListingTranslation(self, listing_id, language, query_params=None, data=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/listings/:listing_id/translations/:language",
        uri_params=[listing_id, language],
        method="POST",
        query_params=query_params
    )
# EndMethod: createListingTranslation


# StartMethod: updateListingTranslation
# uri_parameters: listing_id|language
# http_method: PUT
def updateListingTranslation(self, listing_id, language, query_params=None, data=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/listings/:listing_id/translations/:language",
        uri_params=[listing_id, language],
        method="PUT",
        query_params=query_params
    )
# EndMethod: updateListingTranslation


# StartMethod: deleteListingTranslation
# uri_parameters: listing_id|language
# http_method: DELETE
def deleteListingTranslation(self, listing_id, language, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/listings/:listing_id/translations/:language",
        uri_params=[listing_id, language],
        method="DELETE",
        query_params=query_params
    )
# EndMethod: deleteListingTranslation


# StartMethod: getVariationImages
# uri_parameters: listing_id
# http_method: GET
def getVariationImages(self, listing_id, query_params=None):
    return self.requester.make_request(
        uri="/listings/:listing_id/variation-images",
        uri_params=[listing_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: getVariationImages


# StartMethod: updateVariationImages
# uri_parameters: listing_id
# http_method: POST
def updateVariationImages(self, listing_id, query_params=None, data=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/listings/:listing_id/variation-images",
        uri_params=[listing_id],
        method="POST",
        query_params=query_params
    )
# EndMethod: updateVariationImages


# StartMethod: findAllListingActive
# uri_parameters: 
# http_method: GET
def findAllListingActive(self, query_params=None):
    return self.requester.make_request(
        uri="/listings/active",
        uri_params=[],
        method="GET",
        query_params=query_params
    )
# EndMethod: findAllListingActive


# StartMethod: getInterestingListings
# uri_parameters: 
# http_method: GET
def getInterestingListings(self, query_params=None):
    return self.requester.make_request(
        uri="/listings/interesting",
        uri_params=[],
        method="GET",
        query_params=query_params
    )
# EndMethod: getInterestingListings


# StartMethod: getTrendingListings
# uri_parameters: 
# http_method: GET
def getTrendingListings(self, query_params=None):
    return self.requester.make_request(
        uri="/listings/trending",
        uri_params=[],
        method="GET",
        query_params=query_params
    )
# EndMethod: getTrendingListings


# StartMethod: pagesSignup
# uri_parameters: 
# http_method: POST
def pagesSignup(self, query_params=None, data=None):
    return self.requester.make_request(
        uri="/pages-signup",
        uri_params=[],
        method="POST",
        query_params=query_params
    )
# EndMethod: pagesSignup


# StartMethod: findPage
# uri_parameters: page_id
# http_method: GET
def findPage(self, page_id, query_params=None):
    return self.requester.make_request(
        uri="/pages/:page_id",
        uri_params=[page_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: findPage


# StartMethod: updatePageData
# uri_parameters: page_id
# http_method: POST
def updatePageData(self, page_id, query_params=None, data=None):
    return self.requester.make_request(
        uri="/pages/:page_id",
        uri_params=[page_id],
        method="POST",
        query_params=query_params
    )
# EndMethod: updatePageData


# StartMethod: uploadAvatar
# uri_parameters: page_id
# http_method: POST
def uploadAvatar(self, page_id, query_params=None, data=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/pages/:page_id/avatar",
        uri_params=[page_id],
        method="POST",
        query_params=query_params
    )
# EndMethod: uploadAvatar


# StartMethod: findAllPageCollections
# uri_parameters: page_id
# http_method: GET
def findAllPageCollections(self, page_id, query_params=None):
    return self.requester.make_request(
        uri="/pages/:page_id/collections",
        uri_params=[page_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: findAllPageCollections


# StartMethod: createPageCollection
# uri_parameters: page_id
# http_method: POST
def createPageCollection(self, page_id, query_params=None, data=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/pages/:page_id/collections",
        uri_params=[page_id],
        method="POST",
        query_params=query_params
    )
# EndMethod: createPageCollection


# StartMethod: getPageCollection
# uri_parameters: page_id|collection_id
# http_method: GET
def getPageCollection(self, page_id, collection_id, query_params=None):
    return self.requester.make_request(
        uri="/pages/:page_id/collections/:collection_id",
        uri_params=[page_id, collection_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: getPageCollection


# StartMethod: updatePageCollection
# uri_parameters: page_id|collection_id
# http_method: PUT
def updatePageCollection(self, page_id, collection_id, query_params=None, data=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/pages/:page_id/collections/:collection_id",
        uri_params=[page_id, collection_id],
        method="PUT",
        query_params=query_params
    )
# EndMethod: updatePageCollection


# StartMethod: deletePageCollection
# uri_parameters: page_id|collection_id
# http_method: DELETE
def deletePageCollection(self, page_id, collection_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/pages/:page_id/collections/:collection_id",
        uri_params=[page_id, collection_id],
        method="DELETE",
        query_params=query_params
    )
# EndMethod: deletePageCollection


# StartMethod: getCollectionListings
# uri_parameters: page_id|collection_id
# http_method: GET
def getCollectionListings(self, page_id, collection_id, query_params=None):
    return self.requester.make_request(
        uri="/pages/:page_id/collections/:collection_id/listings",
        uri_params=[page_id, collection_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: getCollectionListings


# StartMethod: addListingToCollection
# uri_parameters: page_id|collection_id|listing_id
# http_method: POST
def addListingToCollection(self, page_id, collection_id, listing_id, query_params=None, data=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/pages/:page_id/collections/:collection_id/listings/:listing_id",
        uri_params=[page_id, collection_id, listing_id],
        method="POST",
        query_params=query_params
    )
# EndMethod: addListingToCollection


# StartMethod: removeListingFromCollection
# uri_parameters: page_id|collection_id|listing_id
# http_method: DELETE
def removeListingFromCollection(self, page_id, collection_id, listing_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/pages/:page_id/collections/:collection_id/listings/:listing_id",
        uri_params=[page_id, collection_id, listing_id],
        method="DELETE",
        query_params=query_params
    )
# EndMethod: removeListingFromCollection


# StartMethod: findPageCollectionsForListings
# uri_parameters: page_id
# http_method: GET
def findPageCollectionsForListings(self, page_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/pages/:page_id/collections/listings_map",
        uri_params=[page_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: findPageCollectionsForListings


# StartMethod: addCurator
# uri_parameters: page_id|curator_id
# http_method: POST
def addCurator(self, page_id, curator_id, query_params=None, data=None):
    return self.requester.make_request(
        uri="/pages/:page_id/curators/:curator_id",
        uri_params=[page_id, curator_id],
        method="POST",
        query_params=query_params
    )
# EndMethod: addCurator


# StartMethod: removeCurator
# uri_parameters: page_id|curator_id
# http_method: DELETE
def removeCurator(self, page_id, curator_id, query_params=None):
    return self.requester.make_request(
        uri="/pages/:page_id/curators/:curator_id",
        uri_params=[page_id, curator_id],
        method="DELETE",
        query_params=query_params
    )
# EndMethod: removeCurator


# StartMethod: curatorPeopleSearch
# uri_parameters: 
# http_method: GET
def curatorPeopleSearch(self, query_params=None):
    return self.requester.make_request(
        uri="/pages/find-curators",
        uri_params=[],
        method="GET",
        query_params=query_params
    )
# EndMethod: curatorPeopleSearch


# StartMethod: findPayment
# uri_parameters: payment_id
# http_method: GET
def findPayment(self, payment_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/payments/:payment_id",
        uri_params=[payment_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: findPayment


# StartMethod: findPaymentAdjustments
# uri_parameters: payment_id
# http_method: GET
def findPaymentAdjustments(self, payment_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/payments/:payment_id/adjustments",
        uri_params=[payment_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: findPaymentAdjustments


# StartMethod: findPaymentAdjustment
# uri_parameters: payment_id|payment_adjustment_id
# http_method: GET
def findPaymentAdjustment(self, payment_id, payment_adjustment_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/payments/:payment_id/adjustments/:payment_adjustment_id",
        uri_params=[payment_id, payment_adjustment_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: findPaymentAdjustment


# StartMethod: findPaymentAdjustmentItems
# uri_parameters: payment_id|payment_adjustment_id
# http_method: GET
def findPaymentAdjustmentItems(self, payment_id, payment_adjustment_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/payments/:payment_id/adjustments/:payment_adjustment_id/items",
        uri_params=[payment_id, payment_adjustment_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: findPaymentAdjustmentItems


# StartMethod: findPaymentAdjustmentItem
# uri_parameters: payment_id|payment_adjustment_id|payment_adjustment_item_id
# http_method: GET
def findPaymentAdjustmentItem(self, payment_id, payment_adjustment_id, payment_adjustment_item_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/payments/:payment_id/adjustments/:payment_adjustment_id/items/:payment_adjustment_item_id",
        uri_params=[payment_id, payment_adjustment_id, payment_adjustment_item_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: findPaymentAdjustmentItem


# StartMethod: getPrivateBaseline
# uri_parameters: 
# http_method: GET
def getPrivateBaseline(self, query_params=None):
    return self.requester.make_request(
        uri="/private-baseline",
        uri_params=[],
        method="GET",
        query_params=query_params
    )
# EndMethod: getPrivateBaseline


# StartMethod: getPropertyOptionModifier
# uri_parameters: 
# http_method: GET
def getPropertyOptionModifier(self, query_params=None):
    return self.requester.make_request(
        uri="/property_options/modifiers",
        uri_params=[],
        method="GET",
        query_params=query_params
    )
# EndMethod: getPropertyOptionModifier


# StartMethod: findAllSuggestedPropertyOptions
# uri_parameters: 
# http_method: GET
def findAllSuggestedPropertyOptions(self, query_params=None):
    return self.requester.make_request(
        uri="/property_options/suggested",
        uri_params=[],
        method="GET",
        query_params=query_params
    )
# EndMethod: findAllSuggestedPropertyOptions


# StartMethod: findPropertySet
# uri_parameters: 
# http_method: GET
def findPropertySet(self, query_params=None):
    return self.requester.make_request(
        uri="/property_sets",
        uri_params=[],
        method="GET",
        query_params=query_params
    )
# EndMethod: findPropertySet


# StartMethod: getShop_Receipt2
# uri_parameters: receipt_id
# http_method: GET
def getShop_Receipt2(self, receipt_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/receipts/:receipt_id",
        uri_params=[receipt_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: getShop_Receipt2


# StartMethod: updateReceipt
# uri_parameters: receipt_id
# http_method: PUT
def updateReceipt(self, receipt_id, query_params=None, data=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/receipts/:receipt_id",
        uri_params=[receipt_id],
        method="PUT",
        query_params=query_params
    )
# EndMethod: updateReceipt


# StartMethod: findAllReceiptListings
# uri_parameters: receipt_id
# http_method: GET
def findAllReceiptListings(self, receipt_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/receipts/:receipt_id/listings",
        uri_params=[receipt_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: findAllReceiptListings


# StartMethod: findAllShop_Receipt2Transactions
# uri_parameters: receipt_id
# http_method: GET
def findAllShop_Receipt2Transactions(self, receipt_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/receipts/:receipt_id/transactions",
        uri_params=[receipt_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: findAllShop_Receipt2Transactions


# StartMethod: findAllRegion
# uri_parameters: 
# http_method: GET
def findAllRegion(self, query_params=None):
    return self.requester.make_request(
        uri="/regions",
        uri_params=[],
        method="GET",
        query_params=query_params
    )
# EndMethod: findAllRegion


# StartMethod: getRegion
# uri_parameters: region_id
# http_method: GET
def getRegion(self, region_id, query_params=None):
    return self.requester.make_request(
        uri="/regions/:region_id",
        uri_params=[region_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: getRegion


# StartMethod: findEligibleRegions
# uri_parameters: 
# http_method: GET
def findEligibleRegions(self, query_params=None):
    return self.requester.make_request(
        uri="/regions/eligible",
        uri_params=[],
        method="GET",
        query_params=query_params
    )
# EndMethod: findEligibleRegions


# StartMethod: getServerEpoch
# uri_parameters: 
# http_method: GET
def getServerEpoch(self, query_params=None):
    return self.requester.make_request(
        uri="/server/epoch",
        uri_params=[],
        method="GET",
        query_params=query_params
    )
# EndMethod: getServerEpoch


# StartMethod: ping
# uri_parameters: 
# http_method: GET
def ping(self, query_params=None):
    return self.requester.make_request(
        uri="/server/ping",
        uri_params=[],
        method="GET",
        query_params=query_params
    )
# EndMethod: ping


# StartMethod: getShippingCosts
# uri_parameters: shipping_provider_id
# http_method: POST
def getShippingCosts(self, shipping_provider_id, query_params=None, data=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/shipping/:shipping_provider_id/postage-costs",
        uri_params=[shipping_provider_id],
        method="POST",
        query_params=query_params
    )
# EndMethod: getShippingCosts


# StartMethod: getShippingInfo
# uri_parameters: shipping_info_id
# http_method: GET
def getShippingInfo(self, shipping_info_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/shipping/info/:shipping_info_id",
        uri_params=[shipping_info_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: getShippingInfo


# StartMethod: updateShippingInfo
# uri_parameters: shipping_info_id
# http_method: PUT
def updateShippingInfo(self, shipping_info_id, query_params=None, data=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/shipping/info/:shipping_info_id",
        uri_params=[shipping_info_id],
        method="PUT",
        query_params=query_params
    )
# EndMethod: updateShippingInfo


# StartMethod: deleteShippingInfo
# uri_parameters: shipping_info_id
# http_method: DELETE
def deleteShippingInfo(self, shipping_info_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/shipping/info/:shipping_info_id",
        uri_params=[shipping_info_id],
        method="DELETE",
        query_params=query_params
    )
# EndMethod: deleteShippingInfo


# StartMethod: getPostageRates
# uri_parameters: shipping_provider_id
# http_method: POST
def getPostageRates(self, shipping_provider_id, query_params=None, data=None):
    return self.requester.make_request(
        uri="/shipping/providers/:shipping_provider_id/mail-class-rates",
        uri_params=[shipping_provider_id],
        method="POST",
        query_params=query_params
    )
# EndMethod: getPostageRates


# StartMethod: createShippingTemplate
# uri_parameters: 
# http_method: POST
def createShippingTemplate(self, query_params=None, data=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/shipping/templates",
        uri_params=[],
        method="POST",
        query_params=query_params
    )
# EndMethod: createShippingTemplate


# StartMethod: getShippingTemplate
# uri_parameters: shipping_template_id
# http_method: GET
def getShippingTemplate(self, shipping_template_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/shipping/templates/:shipping_template_id",
        uri_params=[shipping_template_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: getShippingTemplate


# StartMethod: updateShippingTemplate
# uri_parameters: shipping_template_id
# http_method: PUT
def updateShippingTemplate(self, shipping_template_id, query_params=None, data=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/shipping/templates/:shipping_template_id",
        uri_params=[shipping_template_id],
        method="PUT",
        query_params=query_params
    )
# EndMethod: updateShippingTemplate


# StartMethod: deleteShippingTemplate
# uri_parameters: shipping_template_id
# http_method: DELETE
def deleteShippingTemplate(self, shipping_template_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/shipping/templates/:shipping_template_id",
        uri_params=[shipping_template_id],
        method="DELETE",
        query_params=query_params
    )
# EndMethod: deleteShippingTemplate


# StartMethod: findAllShippingTemplateEntries
# uri_parameters: shipping_template_id
# http_method: GET
def findAllShippingTemplateEntries(self, shipping_template_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/shipping/templates/:shipping_template_id/entries",
        uri_params=[shipping_template_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: findAllShippingTemplateEntries


# StartMethod: findAllShippingTemplateUpgrades
# uri_parameters: shipping_template_id
# http_method: GET
def findAllShippingTemplateUpgrades(self, shipping_template_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/shipping/templates/:shipping_template_id/upgrades",
        uri_params=[shipping_template_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: findAllShippingTemplateUpgrades


# StartMethod: createShippingTemplateUpgrade
# uri_parameters: shipping_template_id
# http_method: POST
def createShippingTemplateUpgrade(self, shipping_template_id, query_params=None, data=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/shipping/templates/:shipping_template_id/upgrades",
        uri_params=[shipping_template_id],
        method="POST",
        query_params=query_params
    )
# EndMethod: createShippingTemplateUpgrade


# StartMethod: updateShippingTemplateUpgrade
# uri_parameters: shipping_template_id
# http_method: PUT
def updateShippingTemplateUpgrade(self, shipping_template_id, query_params=None, data=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/shipping/templates/:shipping_template_id/upgrades",
        uri_params=[shipping_template_id],
        method="PUT",
        query_params=query_params
    )
# EndMethod: updateShippingTemplateUpgrade


# StartMethod: deleteShippingTemplateUpgrade
# uri_parameters: shipping_template_id
# http_method: DELETE
def deleteShippingTemplateUpgrade(self, shipping_template_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/shipping/templates/:shipping_template_id/upgrades",
        uri_params=[shipping_template_id],
        method="DELETE",
        query_params=query_params
    )
# EndMethod: deleteShippingTemplateUpgrade


# StartMethod: createShippingTemplateEntry
# uri_parameters: 
# http_method: POST
def createShippingTemplateEntry(self, query_params=None, data=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/shipping/templates/entries",
        uri_params=[],
        method="POST",
        query_params=query_params
    )
# EndMethod: createShippingTemplateEntry


# StartMethod: getShippingTemplateEntry
# uri_parameters: shipping_template_entry_id
# http_method: GET
def getShippingTemplateEntry(self, shipping_template_entry_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/shipping/templates/entries/:shipping_template_entry_id",
        uri_params=[shipping_template_entry_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: getShippingTemplateEntry


# StartMethod: updateShippingTemplateEntry
# uri_parameters: shipping_template_entry_id
# http_method: PUT
def updateShippingTemplateEntry(self, shipping_template_entry_id, query_params=None, data=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/shipping/templates/entries/:shipping_template_entry_id",
        uri_params=[shipping_template_entry_id],
        method="PUT",
        query_params=query_params
    )
# EndMethod: updateShippingTemplateEntry


# StartMethod: deleteShippingTemplateEntry
# uri_parameters: shipping_template_entry_id
# http_method: DELETE
def deleteShippingTemplateEntry(self, shipping_template_entry_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/shipping/templates/entries/:shipping_template_entry_id",
        uri_params=[shipping_template_entry_id],
        method="DELETE",
        query_params=query_params
    )
# EndMethod: deleteShippingTemplateEntry


# StartMethod: findAllShops
# uri_parameters: 
# http_method: GET
def findAllShops(self, query_params=None):
    return self.requester.make_request(
        uri="/shops",
        uri_params=[],
        method="GET",
        query_params=query_params
    )
# EndMethod: findAllShops


# StartMethod: getShop
# uri_parameters: shop_id
# http_method: GET
def getShop(self, shop_id, query_params=None):
    return self.requester.make_request(
        uri="/shops/:shop_id",
        uri_params=[shop_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: getShop


# StartMethod: updateShop
# uri_parameters: shop_id
# http_method: PUT
def updateShop(self, shop_id, query_params=None, data=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/shops/:shop_id",
        uri_params=[shop_id],
        method="PUT",
        query_params=query_params
    )
# EndMethod: updateShop


# StartMethod: getShopAbout
# uri_parameters: shop_id
# http_method: GET
def getShopAbout(self, shop_id, query_params=None):
    return self.requester.make_request(
        uri="/shops/:shop_id/about",
        uri_params=[shop_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: getShopAbout


# StartMethod: uploadShopBanner
# uri_parameters: shop_id
# http_method: POST
def uploadShopBanner(self, shop_id, query_params=None, data=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/shops/:shop_id/appearance/banner",
        uri_params=[shop_id],
        method="POST",
        query_params=query_params
    )
# EndMethod: uploadShopBanner


# StartMethod: deleteShopBanner
# uri_parameters: shop_id
# http_method: DELETE
def deleteShopBanner(self, shop_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/shops/:shop_id/appearance/banner",
        uri_params=[shop_id],
        method="DELETE",
        query_params=query_params
    )
# EndMethod: deleteShopBanner


# StartMethod: findAllShopCoupons
# uri_parameters: shop_id
# http_method: GET
def findAllShopCoupons(self, shop_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/shops/:shop_id/coupons",
        uri_params=[shop_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: findAllShopCoupons


# StartMethod: createCoupon
# uri_parameters: shop_id
# http_method: POST
def createCoupon(self, shop_id, query_params=None, data=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/shops/:shop_id/coupons",
        uri_params=[shop_id],
        method="POST",
        query_params=query_params
    )
# EndMethod: createCoupon


# StartMethod: findCoupon
# uri_parameters: shop_id|coupon_id
# http_method: GET
def findCoupon(self, shop_id, coupon_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/shops/:shop_id/coupons/:coupon_id",
        uri_params=[shop_id, coupon_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: findCoupon


# StartMethod: updateCoupon
# uri_parameters: shop_id|coupon_id
# http_method: PUT
def updateCoupon(self, shop_id, coupon_id, query_params=None, data=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/shops/:shop_id/coupons/:coupon_id",
        uri_params=[shop_id, coupon_id],
        method="PUT",
        query_params=query_params
    )
# EndMethod: updateCoupon


# StartMethod: deleteCoupon
# uri_parameters: shop_id|coupon_id
# http_method: DELETE
def deleteCoupon(self, shop_id, coupon_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/shops/:shop_id/coupons/:coupon_id",
        uri_params=[shop_id, coupon_id],
        method="DELETE",
        query_params=query_params
    )
# EndMethod: deleteCoupon


# StartMethod: findLedger
# uri_parameters: shop_id
# http_method: GET
def findLedger(self, shop_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/shops/:shop_id/ledger/",
        uri_params=[shop_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: findLedger


# StartMethod: findLedgerEntries
# uri_parameters: shop_id
# http_method: GET
def findLedgerEntries(self, shop_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/shops/:shop_id/ledger/entries",
        uri_params=[shop_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: findLedgerEntries


# StartMethod: findLedgerEntry
# uri_parameters: shop_id|ledger_entry_id
# http_method: GET
def findLedgerEntry(self, shop_id, ledger_entry_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/shops/:shop_id/ledger/entries/:ledger_entry_id",
        uri_params=[shop_id, ledger_entry_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: findLedgerEntry


# StartMethod: findPaymentAdjustmentForLedgerEntry
# uri_parameters: shop_id|ledger_entry_id
# http_method: GET
def findPaymentAdjustmentForLedgerEntry(self, shop_id, ledger_entry_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/shops/:shop_id/ledger/entries/:ledger_entry_id/adjustment",
        uri_params=[shop_id, ledger_entry_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: findPaymentAdjustmentForLedgerEntry


# StartMethod: findPaymentForLedgerEntry
# uri_parameters: shop_id|ledger_entry_id
# http_method: GET
def findPaymentForLedgerEntry(self, shop_id, ledger_entry_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/shops/:shop_id/ledger/entries/:ledger_entry_id/payment",
        uri_params=[shop_id, ledger_entry_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: findPaymentForLedgerEntry


# StartMethod: findAllShopListingsActive
# uri_parameters: shop_id
# http_method: GET
def findAllShopListingsActive(self, shop_id, query_params=None):
    return self.requester.make_request(
        uri="/shops/:shop_id/listings/active",
        uri_params=[shop_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: findAllShopListingsActive


# StartMethod: findAllShopListingsDraft
# uri_parameters: shop_id
# http_method: GET
def findAllShopListingsDraft(self, shop_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/shops/:shop_id/listings/draft",
        uri_params=[shop_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: findAllShopListingsDraft


# StartMethod: findAllShopListingsExpired
# uri_parameters: shop_id
# http_method: GET
def findAllShopListingsExpired(self, shop_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/shops/:shop_id/listings/expired",
        uri_params=[shop_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: findAllShopListingsExpired


# StartMethod: getShopListingExpired
# uri_parameters: shop_id|listing_id
# http_method: GET
def getShopListingExpired(self, shop_id, listing_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/shops/:shop_id/listings/expired/:listing_id",
        uri_params=[shop_id, listing_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: getShopListingExpired


# StartMethod: findAllShopListingsFeatured
# uri_parameters: shop_id
# http_method: GET
def findAllShopListingsFeatured(self, shop_id, query_params=None):
    return self.requester.make_request(
        uri="/shops/:shop_id/listings/featured",
        uri_params=[shop_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: findAllShopListingsFeatured


# StartMethod: findAllShopListingsInactive
# uri_parameters: shop_id
# http_method: GET
def findAllShopListingsInactive(self, shop_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/shops/:shop_id/listings/inactive",
        uri_params=[shop_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: findAllShopListingsInactive


# StartMethod: getShopListingInactive
# uri_parameters: shop_id|listing_id
# http_method: GET
def getShopListingInactive(self, shop_id, listing_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/shops/:shop_id/listings/inactive/:listing_id",
        uri_params=[shop_id, listing_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: getShopListingInactive


# StartMethod: findPaymentAccountEntries
# uri_parameters: shop_id
# http_method: GET
def findPaymentAccountEntries(self, shop_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/shops/:shop_id/payment_account/entries",
        uri_params=[shop_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: findPaymentAccountEntries


# StartMethod: findPaymentAdjustmentForPaymentAccountLedgerEntry
# uri_parameters: shop_id|ledger_entry_id
# http_method: GET
def findPaymentAdjustmentForPaymentAccountLedgerEntry(self, shop_id, ledger_entry_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/shops/:shop_id/payment_account/entries/:ledger_entry_id/adjustment",
        uri_params=[shop_id, ledger_entry_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: findPaymentAdjustmentForPaymentAccountLedgerEntry


# StartMethod: findPaymentForPaymentAccountLedgerEntry
# uri_parameters: shop_id|ledger_entry_id
# http_method: GET
def findPaymentForPaymentAccountLedgerEntry(self, shop_id, ledger_entry_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/shops/:shop_id/payment_account/entries/:ledger_entry_id/payment",
        uri_params=[shop_id, ledger_entry_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: findPaymentForPaymentAccountLedgerEntry


# StartMethod: findShopPaymentTemplates
# uri_parameters: shop_id
# http_method: GET
def findShopPaymentTemplates(self, shop_id, query_params=None):
    return self.requester.make_request(
        uri="/shops/:shop_id/payment_templates",
        uri_params=[shop_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: findShopPaymentTemplates


# StartMethod: createShopPaymentTemplate
# uri_parameters: shop_id
# http_method: POST
def createShopPaymentTemplate(self, shop_id, query_params=None, data=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/shops/:shop_id/payment_templates",
        uri_params=[shop_id],
        method="POST",
        query_params=query_params
    )
# EndMethod: createShopPaymentTemplate


# StartMethod: updateShopPaymentTemplate
# uri_parameters: shop_id|payment_template_id
# http_method: PUT
def updateShopPaymentTemplate(self, shop_id, payment_template_id, query_params=None, data=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/shops/:shop_id/payment_templates/:payment_template_id",
        uri_params=[shop_id, payment_template_id],
        method="PUT",
        query_params=query_params
    )
# EndMethod: updateShopPaymentTemplate


# StartMethod: findAllShopReceipts
# uri_parameters: shop_id
# http_method: GET
def findAllShopReceipts(self, shop_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/shops/:shop_id/receipts",
        uri_params=[shop_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: findAllShopReceipts


# StartMethod: findShopPaymentByReceipt
# uri_parameters: shop_id|receipt_id
# http_method: GET
def findShopPaymentByReceipt(self, shop_id, receipt_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/shops/:shop_id/receipts/:receipt_id/payments",
        uri_params=[shop_id, receipt_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: findShopPaymentByReceipt


# StartMethod: submitTracking
# uri_parameters: shop_id|receipt_id
# http_method: POST
def submitTracking(self, shop_id, receipt_id, query_params=None, data=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/shops/:shop_id/receipts/:receipt_id/tracking",
        uri_params=[shop_id, receipt_id],
        method="POST",
        query_params=query_params
    )
# EndMethod: submitTracking


# StartMethod: findAllShopReceiptsByStatus
# uri_parameters: shop_id|status
# http_method: GET
def findAllShopReceiptsByStatus(self, shop_id, status, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/shops/:shop_id/receipts/:status",
        uri_params=[shop_id, status],
        method="GET",
        query_params=query_params
    )
# EndMethod: findAllShopReceiptsByStatus


# StartMethod: searchAllShopReceipts
# uri_parameters: shop_id
# http_method: GET
def searchAllShopReceipts(self, shop_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/shops/:shop_id/receipts/search",
        uri_params=[shop_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: searchAllShopReceipts


# StartMethod: getShopReviews
# uri_parameters: shop_id
# http_method: GET
def getShopReviews(self, shop_id, query_params=None):
    return self.requester.make_request(
        uri="/shops/:shop_id/reviews",
        uri_params=[shop_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: getShopReviews


# StartMethod: findAllShopSections
# uri_parameters: shop_id
# http_method: GET
def findAllShopSections(self, shop_id, query_params=None):
    return self.requester.make_request(
        uri="/shops/:shop_id/sections",
        uri_params=[shop_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: findAllShopSections


# StartMethod: createShopSection
# uri_parameters: shop_id
# http_method: POST
def createShopSection(self, shop_id, query_params=None, data=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/shops/:shop_id/sections",
        uri_params=[shop_id],
        method="POST",
        query_params=query_params
    )
# EndMethod: createShopSection


# StartMethod: getShopSection
# uri_parameters: shop_id|shop_section_id
# http_method: GET
def getShopSection(self, shop_id, shop_section_id, query_params=None):
    return self.requester.make_request(
        uri="/shops/:shop_id/sections/:shop_section_id",
        uri_params=[shop_id, shop_section_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: getShopSection


# StartMethod: updateShopSection
# uri_parameters: shop_id|shop_section_id
# http_method: PUT
def updateShopSection(self, shop_id, shop_section_id, query_params=None, data=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/shops/:shop_id/sections/:shop_section_id",
        uri_params=[shop_id, shop_section_id],
        method="PUT",
        query_params=query_params
    )
# EndMethod: updateShopSection


# StartMethod: deleteShopSection
# uri_parameters: shop_id|shop_section_id
# http_method: DELETE
def deleteShopSection(self, shop_id, shop_section_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/shops/:shop_id/sections/:shop_section_id",
        uri_params=[shop_id, shop_section_id],
        method="DELETE",
        query_params=query_params
    )
# EndMethod: deleteShopSection


# StartMethod: findAllShopSectionListings
# uri_parameters: shop_id|shop_section_id
# http_method: GET
def findAllShopSectionListings(self, shop_id, shop_section_id, query_params=None):
    return self.requester.make_request(
        uri="/shops/:shop_id/sections/:shop_section_id/listings",
        uri_params=[shop_id, shop_section_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: findAllShopSectionListings


# StartMethod: findAllShopSectionListingsActive
# uri_parameters: shop_id|shop_section_id
# http_method: GET
def findAllShopSectionListingsActive(self, shop_id, shop_section_id, query_params=None):
    return self.requester.make_request(
        uri="/shops/:shop_id/sections/:shop_section_id/listings/active",
        uri_params=[shop_id, shop_section_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: findAllShopSectionListingsActive


# StartMethod: getShopSectionTranslation
# uri_parameters: shop_id|shop_section_id|language
# http_method: GET
def getShopSectionTranslation(self, shop_id, shop_section_id, language, query_params=None):
    return self.requester.make_request(
        uri="/shops/:shop_id/sections/:shop_section_id/translations/:language",
        uri_params=[shop_id, shop_section_id, language],
        method="GET",
        query_params=query_params
    )
# EndMethod: getShopSectionTranslation


# StartMethod: createShopSectionTranslation
# uri_parameters: shop_id|shop_section_id|language
# http_method: POST
def createShopSectionTranslation(self, shop_id, shop_section_id, language, query_params=None, data=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/shops/:shop_id/sections/:shop_section_id/translations/:language",
        uri_params=[shop_id, shop_section_id, language],
        method="POST",
        query_params=query_params
    )
# EndMethod: createShopSectionTranslation


# StartMethod: updateShopSectionTranslation
# uri_parameters: shop_id|shop_section_id|language
# http_method: PUT
def updateShopSectionTranslation(self, shop_id, shop_section_id, language, query_params=None, data=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/shops/:shop_id/sections/:shop_section_id/translations/:language",
        uri_params=[shop_id, shop_section_id, language],
        method="PUT",
        query_params=query_params
    )
# EndMethod: updateShopSectionTranslation


# StartMethod: deleteShopSectionTranslation
# uri_parameters: shop_id|shop_section_id|language
# http_method: DELETE
def deleteShopSectionTranslation(self, shop_id, shop_section_id, language, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/shops/:shop_id/sections/:shop_section_id/translations/:language",
        uri_params=[shop_id, shop_section_id, language],
        method="DELETE",
        query_params=query_params
    )
# EndMethod: deleteShopSectionTranslation


# StartMethod: findAllShopTransactions
# uri_parameters: shop_id
# http_method: GET
def findAllShopTransactions(self, shop_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/shops/:shop_id/transactions",
        uri_params=[shop_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: findAllShopTransactions


# StartMethod: getShopTranslation
# uri_parameters: shop_id|language
# http_method: GET
def getShopTranslation(self, shop_id, language, query_params=None):
    return self.requester.make_request(
        uri="/shops/:shop_id/translations/:language",
        uri_params=[shop_id, language],
        method="GET",
        query_params=query_params
    )
# EndMethod: getShopTranslation


# StartMethod: createShopTranslation
# uri_parameters: shop_id|language
# http_method: POST
def createShopTranslation(self, shop_id, language, query_params=None, data=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/shops/:shop_id/translations/:language",
        uri_params=[shop_id, language],
        method="POST",
        query_params=query_params
    )
# EndMethod: createShopTranslation


# StartMethod: updateShopTranslation
# uri_parameters: shop_id|language
# http_method: PUT
def updateShopTranslation(self, shop_id, language, query_params=None, data=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/shops/:shop_id/translations/:language",
        uri_params=[shop_id, language],
        method="PUT",
        query_params=query_params
    )
# EndMethod: updateShopTranslation


# StartMethod: deleteShopTranslation
# uri_parameters: shop_id|language
# http_method: DELETE
def deleteShopTranslation(self, shop_id, language, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/shops/:shop_id/translations/:language",
        uri_params=[shop_id, language],
        method="DELETE",
        query_params=query_params
    )
# EndMethod: deleteShopTranslation


# StartMethod: getListingShop
# uri_parameters: listing_id
# http_method: GET
def getListingShop(self, listing_id, query_params=None):
    return self.requester.make_request(
        uri="/shops/listing/:listing_id",
        uri_params=[listing_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: getListingShop


# StartMethod: getBuyerTaxonomy
# uri_parameters: 
# http_method: GET
def getBuyerTaxonomy(self, query_params=None):
    return self.requester.make_request(
        uri="/taxonomy/buyer/get",
        uri_params=[],
        method="GET",
        query_params=query_params
    )
# EndMethod: getBuyerTaxonomy


# StartMethod: getTaxonomyNodeProperties
# uri_parameters: taxonomy_id
# http_method: GET
def getTaxonomyNodeProperties(self, taxonomy_id, query_params=None):
    return self.requester.make_request(
        uri="/taxonomy/seller/:taxonomy_id/properties",
        uri_params=[taxonomy_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: getTaxonomyNodeProperties


# StartMethod: getSellerTaxonomy
# uri_parameters: 
# http_method: GET
def getSellerTaxonomy(self, query_params=None):
    return self.requester.make_request(
        uri="/taxonomy/seller/get",
        uri_params=[],
        method="GET",
        query_params=query_params
    )
# EndMethod: getSellerTaxonomy


# StartMethod: getSellerTaxonomyVersion
# uri_parameters: 
# http_method: GET
def getSellerTaxonomyVersion(self, query_params=None):
    return self.requester.make_request(
        uri="/taxonomy/seller/version",
        uri_params=[],
        method="GET",
        query_params=query_params
    )
# EndMethod: getSellerTaxonomyVersion


# StartMethod: findSuggestedStyles
# uri_parameters: 
# http_method: GET
def findSuggestedStyles(self, query_params=None):
    return self.requester.make_request(
        uri="/taxonomy/styles",
        uri_params=[],
        method="GET",
        query_params=query_params
    )
# EndMethod: findSuggestedStyles


# StartMethod: findAllTeams
# uri_parameters: 
# http_method: GET
def findAllTeams(self, query_params=None):
    return self.requester.make_request(
        uri="/teams",
        uri_params=[],
        method="GET",
        query_params=query_params
    )
# EndMethod: findAllTeams


# StartMethod: findAllUsersForTeam
# uri_parameters: team_id
# http_method: GET
def findAllUsersForTeam(self, team_id, query_params=None):
    return self.requester.make_request(
        uri="/teams/:team_id/users/",
        uri_params=[team_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: findAllUsersForTeam


# StartMethod: findTeams
# uri_parameters: team_ids
# http_method: GET
def findTeams(self, team_ids, query_params=None):
    return self.requester.make_request(
        uri="/teams/:team_ids/",
        uri_params=[team_ids],
        method="GET",
        query_params=query_params
    )
# EndMethod: findTeams


# StartMethod: getShop_Transaction
# uri_parameters: transaction_id
# http_method: GET
def getShop_Transaction(self, transaction_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/transactions/:transaction_id",
        uri_params=[transaction_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: getShop_Transaction


# StartMethod: findAllTreasuries
# uri_parameters: 
# http_method: GET
def findAllTreasuries(self, query_params=None):
    return self.requester.make_request(
        uri="/treasuries",
        uri_params=[],
        method="GET",
        query_params=query_params
    )
# EndMethod: findAllTreasuries


# StartMethod: getTreasury
# uri_parameters: treasury_key
# http_method: GET
def getTreasury(self, treasury_key, query_params=None):
    return self.requester.make_request(
        uri="/treasuries/:treasury_key",
        uri_params=[treasury_key],
        method="GET",
        query_params=query_params
    )
# EndMethod: getTreasury


# StartMethod: deleteTreasury
# uri_parameters: treasury_key
# http_method: DELETE
def deleteTreasury(self, treasury_key, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/treasuries/:treasury_key",
        uri_params=[treasury_key],
        method="DELETE",
        query_params=query_params
    )
# EndMethod: deleteTreasury


# StartMethod: findTreasuryComments
# uri_parameters: treasury_key
# http_method: GET
def findTreasuryComments(self, treasury_key, query_params=None):
    return self.requester.make_request(
        uri="/treasuries/:treasury_key/comments",
        uri_params=[treasury_key],
        method="GET",
        query_params=query_params
    )
# EndMethod: findTreasuryComments


# StartMethod: postTreasuryComment
# uri_parameters: treasury_key
# http_method: POST
def postTreasuryComment(self, treasury_key, query_params=None, data=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/treasuries/:treasury_key/comments",
        uri_params=[treasury_key],
        method="POST",
        query_params=query_params
    )
# EndMethod: postTreasuryComment


# StartMethod: deleteTreasuryComment
# uri_parameters: treasury_key|comment_id
# http_method: DELETE
def deleteTreasuryComment(self, treasury_key, comment_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/treasuries/:treasury_key/comments/:comment_id",
        uri_params=[treasury_key, comment_id],
        method="DELETE",
        query_params=query_params
    )
# EndMethod: deleteTreasuryComment


# StartMethod: addTreasuryListing
# uri_parameters: treasury_key
# http_method: POST
def addTreasuryListing(self, treasury_key, query_params=None, data=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/treasuries/:treasury_key/listings",
        uri_params=[treasury_key],
        method="POST",
        query_params=query_params
    )
# EndMethod: addTreasuryListing


# StartMethod: removeTreasuryListing
# uri_parameters: treasury_key|listing_id
# http_method: DELETE
def removeTreasuryListing(self, treasury_key, listing_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/treasuries/:treasury_key/listings/:listing_id",
        uri_params=[treasury_key, listing_id],
        method="DELETE",
        query_params=query_params
    )
# EndMethod: removeTreasuryListing


# StartMethod: describeOccasionEnum
# uri_parameters: 
# http_method: GET
def describeOccasionEnum(self, query_params=None):
    return self.requester.make_request(
        uri="/types/enum/occasion",
        uri_params=[],
        method="GET",
        query_params=query_params
    )
# EndMethod: describeOccasionEnum


# StartMethod: describeRecipientEnum
# uri_parameters: 
# http_method: GET
def describeRecipientEnum(self, query_params=None):
    return self.requester.make_request(
        uri="/types/enum/recipient",
        uri_params=[],
        method="GET",
        query_params=query_params
    )
# EndMethod: describeRecipientEnum


# StartMethod: describeWhenMadeEnum
# uri_parameters: 
# http_method: GET
def describeWhenMadeEnum(self, query_params=None):
    return self.requester.make_request(
        uri="/types/enum/when_made",
        uri_params=[],
        method="GET",
        query_params=query_params
    )
# EndMethod: describeWhenMadeEnum


# StartMethod: describeWhoMadeEnum
# uri_parameters: 
# http_method: GET
def describeWhoMadeEnum(self, query_params=None):
    return self.requester.make_request(
        uri="/types/enum/who_made",
        uri_params=[],
        method="GET",
        query_params=query_params
    )
# EndMethod: describeWhoMadeEnum


# StartMethod: findAllUsers
# uri_parameters: 
# http_method: GET
def findAllUsers(self, query_params=None):
    return self.requester.make_request(
        uri="/users",
        uri_params=[],
        method="GET",
        query_params=query_params
    )
# EndMethod: findAllUsers


# StartMethod: getUser
# uri_parameters: user_id
# http_method: GET
def getUser(self, user_id, query_params=None):
    return self.requester.make_request(
        uri="/users/:user_id",
        uri_params=[user_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: getUser


# StartMethod: findAllUserAddresses
# uri_parameters: user_id
# http_method: GET
def findAllUserAddresses(self, user_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/users/:user_id/addresses",
        uri_params=[user_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: findAllUserAddresses


# StartMethod: createUserAddress
# uri_parameters: user_id
# http_method: POST
def createUserAddress(self, user_id, query_params=None, data=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/users/:user_id/addresses/",
        uri_params=[user_id],
        method="POST",
        query_params=query_params
    )
# EndMethod: createUserAddress


# StartMethod: getUserAddress
# uri_parameters: user_id|user_address_id
# http_method: GET
def getUserAddress(self, user_id, user_address_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/users/:user_id/addresses/:user_address_id",
        uri_params=[user_id, user_address_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: getUserAddress


# StartMethod: deleteUserAddress
# uri_parameters: user_id|user_address_id
# http_method: DELETE
def deleteUserAddress(self, user_id, user_address_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/users/:user_id/addresses/:user_address_id",
        uri_params=[user_id, user_address_id],
        method="DELETE",
        query_params=query_params
    )
# EndMethod: deleteUserAddress


# StartMethod: uploadAvatar
# uri_parameters: user_id
# http_method: POST
def uploadAvatar(self, user_id, query_params=None, data=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/users/:user_id/avatar",
        uri_params=[user_id],
        method="POST",
        query_params=query_params
    )
# EndMethod: uploadAvatar


# StartMethod: getAvatarImgSrc
# uri_parameters: user_id
# http_method: GET
def getAvatarImgSrc(self, user_id, query_params=None):
    return self.requester.make_request(
        uri="/users/:user_id/avatar/src",
        uri_params=[user_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: getAvatarImgSrc


# StartMethod: getUserBillingOverview
# uri_parameters: user_id
# http_method: GET
def getUserBillingOverview(self, user_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/users/:user_id/billing/overview",
        uri_params=[user_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: getUserBillingOverview


# StartMethod: getAllUserCarts
# uri_parameters: user_id
# http_method: GET
def getAllUserCarts(self, user_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/users/:user_id/carts",
        uri_params=[user_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: getAllUserCarts


# StartMethod: addToCart
# uri_parameters: user_id
# http_method: POST
def addToCart(self, user_id, query_params=None, data=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/users/:user_id/carts",
        uri_params=[user_id],
        method="POST",
        query_params=query_params
    )
# EndMethod: addToCart


# StartMethod: updateCartListingQuantity
# uri_parameters: user_id
# http_method: PUT
def updateCartListingQuantity(self, user_id, query_params=None, data=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/users/:user_id/carts",
        uri_params=[user_id],
        method="PUT",
        query_params=query_params
    )
# EndMethod: updateCartListingQuantity


# StartMethod: removeCartListing
# uri_parameters: user_id
# http_method: DELETE
def removeCartListing(self, user_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/users/:user_id/carts",
        uri_params=[user_id],
        method="DELETE",
        query_params=query_params
    )
# EndMethod: removeCartListing


# StartMethod: getUserCart
# uri_parameters: user_id|cart_id
# http_method: GET
def getUserCart(self, user_id, cart_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/users/:user_id/carts/:cart_id",
        uri_params=[user_id, cart_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: getUserCart


# StartMethod: updateCart
# uri_parameters: user_id|cart_id
# http_method: PUT
def updateCart(self, user_id, cart_id, query_params=None, data=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/users/:user_id/carts/:cart_id",
        uri_params=[user_id, cart_id],
        method="PUT",
        query_params=query_params
    )
# EndMethod: updateCart


# StartMethod: deleteCart
# uri_parameters: user_id|cart_id
# http_method: DELETE
def deleteCart(self, user_id, cart_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/users/:user_id/carts/:cart_id",
        uri_params=[user_id, cart_id],
        method="DELETE",
        query_params=query_params
    )
# EndMethod: deleteCart


# StartMethod: addAndSelectShippingForApplePay
# uri_parameters: user_id|cart_id
# http_method: POST
def addAndSelectShippingForApplePay(self, user_id, cart_id, query_params=None, data=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/users/:user_id/carts/:cart_id/add_and_select_shipping_for_apple",
        uri_params=[user_id, cart_id],
        method="POST",
        query_params=query_params
    )
# EndMethod: addAndSelectShippingForApplePay


# StartMethod: findAllCartListings
# uri_parameters: user_id|cart_id
# http_method: GET
def findAllCartListings(self, user_id, cart_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/users/:user_id/carts/:cart_id/listings",
        uri_params=[user_id, cart_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: findAllCartListings


# StartMethod: saveListingForLater
# uri_parameters: user_id
# http_method: DELETE
def saveListingForLater(self, user_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/users/:user_id/carts/save",
        uri_params=[user_id],
        method="DELETE",
        query_params=query_params
    )
# EndMethod: saveListingForLater


# StartMethod: getUserCartForShop
# uri_parameters: user_id|shop_id
# http_method: GET
def getUserCartForShop(self, user_id, shop_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/users/:user_id/carts/shop/:shop_id",
        uri_params=[user_id, shop_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: getUserCartForShop


# StartMethod: createSingleListingCart
# uri_parameters: user_id
# http_method: POST
def createSingleListingCart(self, user_id, query_params=None, data=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/users/:user_id/carts/single_listing",
        uri_params=[user_id],
        method="POST",
        query_params=query_params
    )
# EndMethod: createSingleListingCart


# StartMethod: findAllUserCharges
# uri_parameters: user_id
# http_method: GET
def findAllUserCharges(self, user_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/users/:user_id/charges",
        uri_params=[user_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: findAllUserCharges


# StartMethod: getUserChargesMetadata
# uri_parameters: user_id
# http_method: GET
def getUserChargesMetadata(self, user_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/users/:user_id/charges/meta",
        uri_params=[user_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: getUserChargesMetadata


# StartMethod: getCirclesContainingUser
# uri_parameters: user_id
# http_method: GET
def getCirclesContainingUser(self, user_id, query_params=None):
    return self.requester.make_request(
        uri="/users/:user_id/circles",
        uri_params=[user_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: getCirclesContainingUser


# StartMethod: getConnectedUser
# uri_parameters: user_id|to_user_id
# http_method: GET
def getConnectedUser(self, user_id, to_user_id, query_params=None):
    return self.requester.make_request(
        uri="/users/:user_id/circles/:to_user_id",
        uri_params=[user_id, to_user_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: getConnectedUser


# StartMethod: unconnectUsers
# uri_parameters: user_id|to_user_id
# http_method: DELETE
def unconnectUsers(self, user_id, to_user_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/users/:user_id/circles/:to_user_id",
        uri_params=[user_id, to_user_id],
        method="DELETE",
        query_params=query_params
    )
# EndMethod: unconnectUsers


# StartMethod: listFollowingPages
# uri_parameters: user_id
# http_method: GET
def listFollowingPages(self, user_id, query_params=None):
    return self.requester.make_request(
        uri="/users/:user_id/connected_pages",
        uri_params=[user_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: listFollowingPages


# StartMethod: followPage
# uri_parameters: user_id
# http_method: POST
def followPage(self, user_id, query_params=None, data=None):
    return self.requester.make_request(
        uri="/users/:user_id/connected_pages",
        uri_params=[user_id],
        method="POST",
        query_params=query_params
    )
# EndMethod: followPage


# StartMethod: unfollowPage
# uri_parameters: user_id|page_id
# http_method: DELETE
def unfollowPage(self, user_id, page_id, query_params=None):
    return self.requester.make_request(
        uri="/users/:user_id/connected_pages/:page_id",
        uri_params=[user_id, page_id],
        method="DELETE",
        query_params=query_params
    )
# EndMethod: unfollowPage


# StartMethod: getConnectedUsers
# uri_parameters: user_id
# http_method: GET
def getConnectedUsers(self, user_id, query_params=None):
    return self.requester.make_request(
        uri="/users/:user_id/connected_users",
        uri_params=[user_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: getConnectedUsers


# StartMethod: connectUsers
# uri_parameters: user_id
# http_method: POST
def connectUsers(self, user_id, query_params=None, data=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/users/:user_id/connected_users",
        uri_params=[user_id],
        method="POST",
        query_params=query_params
    )
# EndMethod: connectUsers


# StartMethod: findAllUserFavoredBy
# uri_parameters: user_id
# http_method: GET
def findAllUserFavoredBy(self, user_id, query_params=None):
    return self.requester.make_request(
        uri="/users/:user_id/favored-by",
        uri_params=[user_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: findAllUserFavoredBy


# StartMethod: findAllUserFavoriteListings
# uri_parameters: user_id
# http_method: GET
def findAllUserFavoriteListings(self, user_id, query_params=None):
    return self.requester.make_request(
        uri="/users/:user_id/favorites/listings",
        uri_params=[user_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: findAllUserFavoriteListings


# StartMethod: findUserFavoriteListings
# uri_parameters: user_id|listing_id
# http_method: GET
def findUserFavoriteListings(self, user_id, listing_id, query_params=None):
    return self.requester.make_request(
        uri="/users/:user_id/favorites/listings/:listing_id",
        uri_params=[user_id, listing_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: findUserFavoriteListings


# StartMethod: createUserFavoriteListings
# uri_parameters: user_id|listing_id
# http_method: POST
def createUserFavoriteListings(self, user_id, listing_id, query_params=None, data=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/users/:user_id/favorites/listings/:listing_id",
        uri_params=[user_id, listing_id],
        method="POST",
        query_params=query_params
    )
# EndMethod: createUserFavoriteListings


# StartMethod: deleteUserFavoriteListings
# uri_parameters: user_id|listing_id
# http_method: DELETE
def deleteUserFavoriteListings(self, user_id, listing_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/users/:user_id/favorites/listings/:listing_id",
        uri_params=[user_id, listing_id],
        method="DELETE",
        query_params=query_params
    )
# EndMethod: deleteUserFavoriteListings


# StartMethod: findAllUserFavoriteUsers
# uri_parameters: user_id
# http_method: GET
def findAllUserFavoriteUsers(self, user_id, query_params=None):
    return self.requester.make_request(
        uri="/users/:user_id/favorites/users",
        uri_params=[user_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: findAllUserFavoriteUsers


# StartMethod: findUserFavoriteUsers
# uri_parameters: user_id|target_user_id
# http_method: GET
def findUserFavoriteUsers(self, user_id, target_user_id, query_params=None):
    return self.requester.make_request(
        uri="/users/:user_id/favorites/users/:target_user_id",
        uri_params=[user_id, target_user_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: findUserFavoriteUsers


# StartMethod: createUserFavoriteUsers
# uri_parameters: user_id|target_user_id
# http_method: POST
def createUserFavoriteUsers(self, user_id, target_user_id, query_params=None, data=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/users/:user_id/favorites/users/:target_user_id",
        uri_params=[user_id, target_user_id],
        method="POST",
        query_params=query_params
    )
# EndMethod: createUserFavoriteUsers


# StartMethod: deleteUserFavoriteUsers
# uri_parameters: user_id|target_user_id
# http_method: DELETE
def deleteUserFavoriteUsers(self, user_id, target_user_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/users/:user_id/favorites/users/:target_user_id",
        uri_params=[user_id, target_user_id],
        method="DELETE",
        query_params=query_params
    )
# EndMethod: deleteUserFavoriteUsers


# StartMethod: findAllUserFeedbackAsAuthor
# uri_parameters: user_id
# http_method: GET
def findAllUserFeedbackAsAuthor(self, user_id, query_params=None):
    return self.requester.make_request(
        uri="/users/:user_id/feedback/as-author",
        uri_params=[user_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: findAllUserFeedbackAsAuthor


# StartMethod: findAllUserFeedbackAsBuyer
# uri_parameters: user_id
# http_method: GET
def findAllUserFeedbackAsBuyer(self, user_id, query_params=None):
    return self.requester.make_request(
        uri="/users/:user_id/feedback/as-buyer",
        uri_params=[user_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: findAllUserFeedbackAsBuyer


# StartMethod: findAllUserFeedbackAsSeller
# uri_parameters: user_id
# http_method: GET
def findAllUserFeedbackAsSeller(self, user_id, query_params=None):
    return self.requester.make_request(
        uri="/users/:user_id/feedback/as-seller",
        uri_params=[user_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: findAllUserFeedbackAsSeller


# StartMethod: findAllUserFeedbackAsSubject
# uri_parameters: user_id
# http_method: GET
def findAllUserFeedbackAsSubject(self, user_id, query_params=None):
    return self.requester.make_request(
        uri="/users/:user_id/feedback/as-subject",
        uri_params=[user_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: findAllUserFeedbackAsSubject


# StartMethod: findAllFeedbackFromBuyers
# uri_parameters: user_id
# http_method: GET
def findAllFeedbackFromBuyers(self, user_id, query_params=None):
    return self.requester.make_request(
        uri="/users/:user_id/feedback/from-buyers",
        uri_params=[user_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: findAllFeedbackFromBuyers


# StartMethod: findAllFeedbackFromSellers
# uri_parameters: user_id
# http_method: GET
def findAllFeedbackFromSellers(self, user_id, query_params=None):
    return self.requester.make_request(
        uri="/users/:user_id/feedback/from-sellers",
        uri_params=[user_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: findAllFeedbackFromSellers


# StartMethod: findAllUserPayments
# uri_parameters: user_id
# http_method: GET
def findAllUserPayments(self, user_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/users/:user_id/payments",
        uri_params=[user_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: findAllUserPayments


# StartMethod: findAllUserPaymentTemplates
# uri_parameters: user_id
# http_method: GET
def findAllUserPaymentTemplates(self, user_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/users/:user_id/payments/templates",
        uri_params=[user_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: findAllUserPaymentTemplates


# StartMethod: findUserProfile
# uri_parameters: user_id
# http_method: GET
def findUserProfile(self, user_id, query_params=None):
    return self.requester.make_request(
        uri="/users/:user_id/profile",
        uri_params=[user_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: findUserProfile


# StartMethod: updateUserProfile
# uri_parameters: user_id
# http_method: PUT
def updateUserProfile(self, user_id, query_params=None, data=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/users/:user_id/profile",
        uri_params=[user_id],
        method="PUT",
        query_params=query_params
    )
# EndMethod: updateUserProfile


# StartMethod: findAllUserBuyerReceipts
# uri_parameters: user_id
# http_method: GET
def findAllUserBuyerReceipts(self, user_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/users/:user_id/receipts",
        uri_params=[user_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: findAllUserBuyerReceipts


# StartMethod: findAllUserShippingProfiles
# uri_parameters: user_id
# http_method: GET
def findAllUserShippingProfiles(self, user_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/users/:user_id/shipping/templates",
        uri_params=[user_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: findAllUserShippingProfiles


# StartMethod: findAllUserShops
# uri_parameters: user_id
# http_method: GET
def findAllUserShops(self, user_id, query_params=None):
    return self.requester.make_request(
        uri="/users/:user_id/shops",
        uri_params=[user_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: findAllUserShops


# StartMethod: findAllTeamsForUser
# uri_parameters: user_id
# http_method: GET
def findAllTeamsForUser(self, user_id, query_params=None):
    return self.requester.make_request(
        uri="/users/:user_id/teams",
        uri_params=[user_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: findAllTeamsForUser


# StartMethod: findAllUserBuyerTransactions
# uri_parameters: user_id
# http_method: GET
def findAllUserBuyerTransactions(self, user_id, query_params=None):
    if self.requester.auth_mode == "api_key":
        raise RequiresOauth
    
    return self.requester.make_request(
        uri="/users/:user_id/transactions",
        uri_params=[user_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: findAllUserBuyerTransactions


# StartMethod: findAllUserTreasuries
# uri_parameters: user_id
# http_method: GET
def findAllUserTreasuries(self, user_id, query_params=None):
    return self.requester.make_request(
        uri="/users/:user_id/treasuries",
        uri_params=[user_id],
        method="GET",
        query_params=query_params
    )
# EndMethod: findAllUserTreasuries
