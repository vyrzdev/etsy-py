from .rq import RequiresOauth


# These methods are all auto-generated from the Etsy Method Table, by updater.py periodically


# Any manual changes will be overwritten!

# StartMethod: getMethodTable
def getMethodTable(self, query_params=None):
    return self.requester.make_request(uri='/', uri_params=[], method='GET', query_params=query_params,)
# EndMethod: getMethodTable


# StartMethod: getPublicBaseline
def getPublicBaseline(self, query_params=None):
    return self.requester.make_request(uri='/baseline', uri_params=[], method='GET', query_params=query_params,)
# EndMethod: getPublicBaseline


# StartMethod: findAllCountry
def findAllCountry(self, query_params=None):
    return self.requester.make_request(uri='/countries', uri_params=[], method='GET', query_params=query_params,)
# EndMethod: findAllCountry


# StartMethod: getCountry
def getCountry(self, country_id, query_params=None):
    return self.requester.make_request(uri='/countries/:country_id', uri_params=[ country_id,], method='GET', query_params=query_params,)
# EndMethod: getCountry


# StartMethod: findByIsoCode
def findByIsoCode(self, iso_code, query_params=None):
    return self.requester.make_request(uri='/countries/iso/:iso_code', uri_params=[ iso_code,], method='GET', query_params=query_params,)
# EndMethod: findByIsoCode


# StartMethod: findAllFeaturedTreasuries
def findAllFeaturedTreasuries(self, query_params=None):
    return self.requester.make_request(uri='/featured_treasuries', uri_params=[], method='GET', query_params=query_params,)
# EndMethod: findAllFeaturedTreasuries


# StartMethod: getFeaturedTreasuryById
def getFeaturedTreasuryById(self, featured_treasury_id, query_params=None):
    return self.requester.make_request(uri='/featured_treasuries/:featured_treasury_id', uri_params=[ featured_treasury_id,], method='GET', query_params=query_params,)
# EndMethod: getFeaturedTreasuryById


# StartMethod: findAllListingsForFeaturedTreasuryId
def findAllListingsForFeaturedTreasuryId(self, featured_treasury_id, query_params=None):
    return self.requester.make_request(uri='/featured_treasuries/:featured_treasury_id/listings', uri_params=[ featured_treasury_id,], method='GET', query_params=query_params,)
# EndMethod: findAllListingsForFeaturedTreasuryId


# StartMethod: findAllActiveListingsForFeaturedTreasuryId
def findAllActiveListingsForFeaturedTreasuryId(self, featured_treasury_id, query_params=None):
    return self.requester.make_request(uri='/featured_treasuries/:featured_treasury_id/listings/active', uri_params=[ featured_treasury_id,], method='GET', query_params=query_params,)
# EndMethod: findAllActiveListingsForFeaturedTreasuryId


# StartMethod: findAllFeaturedListings
def findAllFeaturedListings(self, query_params=None):
    return self.requester.make_request(uri='/featured_treasuries/listings', uri_params=[], method='GET', query_params=query_params,)
# EndMethod: findAllFeaturedListings


# StartMethod: findAllCurrentFeaturedListings
def findAllCurrentFeaturedListings(self, query_params=None):
    return self.requester.make_request(uri='/featured_treasuries/listings/homepage_current', uri_params=[], method='GET', query_params=query_params,)
# EndMethod: findAllCurrentFeaturedListings


# StartMethod: findAllFeaturedTreasuriesByOwner
def findAllFeaturedTreasuriesByOwner(self, owner_id, query_params=None):
    return self.requester.make_request(uri='/featured_treasuries/owner/:owner_id', uri_params=[ owner_id,], method='GET', query_params=query_params,)
# EndMethod: findAllFeaturedTreasuriesByOwner


# StartMethod: getGuest
def getGuest(self, guest_id, query_params=None):
    return self.requester.make_request(uri='/guests/:guest_id', uri_params=[ guest_id,], method='GET', query_params=query_params,)
# EndMethod: getGuest


# StartMethod: findAllGuestCarts
def findAllGuestCarts(self, guest_id, query_params=None):
    return self.requester.make_request(uri='/guests/:guest_id/carts', uri_params=[ guest_id,], method='GET', query_params=query_params,)
# EndMethod: findAllGuestCarts


# StartMethod: addToGuestCart
def addToGuestCart(self, guest_id, data=None, query_params=None):
    return self.requester.make_request(uri='/guests/:guest_id/carts', uri_params=[ guest_id,], method='POST', query_params=query_params, data=data,)
# EndMethod: addToGuestCart


# StartMethod: updateGuestCartListingQuantity
def updateGuestCartListingQuantity(self, guest_id, data=None, query_params=None):
    return self.requester.make_request(uri='/guests/:guest_id/carts', uri_params=[ guest_id,], method='PUT', query_params=query_params, data=data,)
# EndMethod: updateGuestCartListingQuantity


# StartMethod: removeGuestCartListing
def removeGuestCartListing(self, guest_id, query_params=None):
    return self.requester.make_request(uri='/guests/:guest_id/carts', uri_params=[ guest_id,], method='DELETE', query_params=query_params,)
# EndMethod: removeGuestCartListing


# StartMethod: findGuestCart
def findGuestCart(self, guest_id, cart_id, query_params=None):
    return self.requester.make_request(uri='/guests/:guest_id/carts/:cart_id', uri_params=[ guest_id, cart_id,], method='GET', query_params=query_params,)
# EndMethod: findGuestCart


# StartMethod: updateGuestCart
def updateGuestCart(self, guest_id, cart_id, data=None, query_params=None):
    return self.requester.make_request(uri='/guests/:guest_id/carts/:cart_id', uri_params=[ guest_id, cart_id,], method='PUT', query_params=query_params, data=data,)
# EndMethod: updateGuestCart


# StartMethod: deleteGuestCart
def deleteGuestCart(self, guest_id, cart_id, query_params=None):
    return self.requester.make_request(uri='/guests/:guest_id/carts/:cart_id', uri_params=[ guest_id, cart_id,], method='DELETE', query_params=query_params,)
# EndMethod: deleteGuestCart


# StartMethod: claimGuest
def claimGuest(self, guest_id, data=None, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/guests/:guest_id/claim', uri_params=[ guest_id,], method='POST', query_params=query_params, data=data,)
# EndMethod: claimGuest


# StartMethod: mergeGuest
def mergeGuest(self, guest_id, data=None, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/guests/:guest_id/merge', uri_params=[ guest_id,], method='POST', query_params=query_params, data=data,)
# EndMethod: mergeGuest


# StartMethod: generateGuest
def generateGuest(self, query_params=None):
    return self.requester.make_request(uri='/guests/generator', uri_params=[], method='GET', query_params=query_params,)
# EndMethod: generateGuest


# StartMethod: listImageTypes
def listImageTypes(self, query_params=None):
    return self.requester.make_request(uri='/image_types', uri_params=[], method='GET', query_params=query_params,)
# EndMethod: listImageTypes


# StartMethod: createListing
def createListing(self, data=None, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/listings', uri_params=[], method='POST', query_params=query_params, data=data,)
# EndMethod: createListing


# StartMethod: getListing
def getListing(self, listing_id, query_params=None):
    return self.requester.make_request(uri='/listings/:listing_id', uri_params=[ listing_id,], method='GET', query_params=query_params,)
# EndMethod: getListing


# StartMethod: updateListing
def updateListing(self, listing_id, data=None, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/listings/:listing_id', uri_params=[ listing_id,], method='PUT', query_params=query_params, data=data,)
# EndMethod: updateListing


# StartMethod: deleteListing
def deleteListing(self, listing_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/listings/:listing_id', uri_params=[ listing_id,], method='DELETE', query_params=query_params,)
# EndMethod: deleteListing


# StartMethod: getAttributes
def getAttributes(self, listing_id, query_params=None):
    return self.requester.make_request(uri='/listings/:listing_id/attributes', uri_params=[ listing_id,], method='GET', query_params=query_params,)
# EndMethod: getAttributes


# StartMethod: getAttribute
def getAttribute(self, listing_id, property_id, query_params=None):
    return self.requester.make_request(uri='/listings/:listing_id/attributes/:property_id', uri_params=[ listing_id, property_id,], method='GET', query_params=query_params,)
# EndMethod: getAttribute


# StartMethod: updateAttribute
def updateAttribute(self, listing_id, property_id, data=None, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/listings/:listing_id/attributes/:property_id', uri_params=[ listing_id, property_id,], method='PUT', query_params=query_params, data=data,)
# EndMethod: updateAttribute


# StartMethod: deleteAttribute
def deleteAttribute(self, listing_id, property_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/listings/:listing_id/attributes/:property_id', uri_params=[ listing_id, property_id,], method='DELETE', query_params=query_params,)
# EndMethod: deleteAttribute


# StartMethod: findAllListingFavoredBy
def findAllListingFavoredBy(self, listing_id, query_params=None):
    return self.requester.make_request(uri='/listings/:listing_id/favored-by', uri_params=[ listing_id,], method='GET', query_params=query_params,)
# EndMethod: findAllListingFavoredBy


# StartMethod: findAllListingFiles
def findAllListingFiles(self, listing_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/listings/:listing_id/files', uri_params=[ listing_id,], method='GET', query_params=query_params,)
# EndMethod: findAllListingFiles


# StartMethod: uploadListingFile
def uploadListingFile(self, listing_id, data=None, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/listings/:listing_id/files', uri_params=[ listing_id,], method='POST', query_params=query_params, data=data,)
# EndMethod: uploadListingFile


# StartMethod: findListingFile
def findListingFile(self, listing_id, listing_file_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/listings/:listing_id/files/:listing_file_id', uri_params=[ listing_id, listing_file_id,], method='GET', query_params=query_params,)
# EndMethod: findListingFile


# StartMethod: deleteListingFile
def deleteListingFile(self, listing_id, listing_file_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/listings/:listing_id/files/:listing_file_id', uri_params=[ listing_id, listing_file_id,], method='DELETE', query_params=query_params,)
# EndMethod: deleteListingFile


# StartMethod: findAllListingImages
def findAllListingImages(self, listing_id, query_params=None):
    return self.requester.make_request(uri='/listings/:listing_id/images', uri_params=[ listing_id,], method='GET', query_params=query_params,)
# EndMethod: findAllListingImages


# StartMethod: uploadListingImage
def uploadListingImage(self, listing_id, data=None, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/listings/:listing_id/images', uri_params=[ listing_id,], method='POST', query_params=query_params, data=data,)
# EndMethod: uploadListingImage


# StartMethod: getImage_Listing
def getImage_Listing(self, listing_id, listing_image_id, query_params=None):
    return self.requester.make_request(uri='/listings/:listing_id/images/:listing_image_id', uri_params=[ listing_id, listing_image_id,], method='GET', query_params=query_params,)
# EndMethod: getImage_Listing


# StartMethod: deleteListingImage
def deleteListingImage(self, listing_id, listing_image_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/listings/:listing_id/images/:listing_image_id', uri_params=[ listing_id, listing_image_id,], method='DELETE', query_params=query_params,)
# EndMethod: deleteListingImage


# StartMethod: getInventory
def getInventory(self, listing_id, query_params=None):
    return self.requester.make_request(uri='/listings/:listing_id/inventory', uri_params=[ listing_id,], method='GET', query_params=query_params,)
# EndMethod: getInventory


# StartMethod: updateInventory
def updateInventory(self, listing_id, data=None, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/listings/:listing_id/inventory', uri_params=[ listing_id,], method='PUT', query_params=query_params, data=data,)
# EndMethod: updateInventory


# StartMethod: getProduct
def getProduct(self, listing_id, product_id, query_params=None):
    return self.requester.make_request(uri='/listings/:listing_id/products/:product_id', uri_params=[ listing_id, product_id,], method='GET', query_params=query_params,)
# EndMethod: getProduct


# StartMethod: getOffering
def getOffering(self, listing_id, product_id, offering_id, query_params=None):
    return self.requester.make_request(uri='/listings/:listing_id/products/:product_id/offerings/:offering_id', uri_params=[ listing_id, product_id, offering_id,], method='GET', query_params=query_params,)
# EndMethod: getOffering


# StartMethod: findAllListingShippingProfileEntries
def findAllListingShippingProfileEntries(self, listing_id, query_params=None):
    return self.requester.make_request(uri='/listings/:listing_id/shipping/info', uri_params=[ listing_id,], method='GET', query_params=query_params,)
# EndMethod: findAllListingShippingProfileEntries


# StartMethod: createShippingInfo
def createShippingInfo(self, listing_id, data=None, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/listings/:listing_id/shipping/info', uri_params=[ listing_id,], method='POST', query_params=query_params, data=data,)
# EndMethod: createShippingInfo


# StartMethod: getListingShippingUpgrades
def getListingShippingUpgrades(self, listing_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/listings/:listing_id/shipping/upgrades', uri_params=[ listing_id,], method='GET', query_params=query_params,)
# EndMethod: getListingShippingUpgrades


# StartMethod: createListingShippingUpgrade
def createListingShippingUpgrade(self, listing_id, data=None, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/listings/:listing_id/shipping/upgrades', uri_params=[ listing_id,], method='POST', query_params=query_params, data=data,)
# EndMethod: createListingShippingUpgrade


# StartMethod: updateListingShippingUpgrade
def updateListingShippingUpgrade(self, listing_id, data=None, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/listings/:listing_id/shipping/upgrades', uri_params=[ listing_id,], method='PUT', query_params=query_params, data=data,)
# EndMethod: updateListingShippingUpgrade


# StartMethod: deleteListingShippingUpgrade
def deleteListingShippingUpgrade(self, listing_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/listings/:listing_id/shipping/upgrades', uri_params=[ listing_id,], method='DELETE', query_params=query_params,)
# EndMethod: deleteListingShippingUpgrade


# StartMethod: findAllListingTransactions
def findAllListingTransactions(self, listing_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/listings/:listing_id/transactions', uri_params=[ listing_id,], method='GET', query_params=query_params,)
# EndMethod: findAllListingTransactions


# StartMethod: getListingTranslation
def getListingTranslation(self, listing_id, language, query_params=None):
    return self.requester.make_request(uri='/listings/:listing_id/translations/:language', uri_params=[ listing_id, language,], method='GET', query_params=query_params,)
# EndMethod: getListingTranslation


# StartMethod: createListingTranslation
def createListingTranslation(self, listing_id, language, data=None, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/listings/:listing_id/translations/:language', uri_params=[ listing_id, language,], method='POST', query_params=query_params, data=data,)
# EndMethod: createListingTranslation


# StartMethod: updateListingTranslation
def updateListingTranslation(self, listing_id, language, data=None, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/listings/:listing_id/translations/:language', uri_params=[ listing_id, language,], method='PUT', query_params=query_params, data=data,)
# EndMethod: updateListingTranslation


# StartMethod: deleteListingTranslation
def deleteListingTranslation(self, listing_id, language, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/listings/:listing_id/translations/:language', uri_params=[ listing_id, language,], method='DELETE', query_params=query_params,)
# EndMethod: deleteListingTranslation


# StartMethod: getVariationImages
def getVariationImages(self, listing_id, query_params=None):
    return self.requester.make_request(uri='/listings/:listing_id/variation-images', uri_params=[ listing_id,], method='GET', query_params=query_params,)
# EndMethod: getVariationImages


# StartMethod: updateVariationImages
def updateVariationImages(self, listing_id, data=None, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/listings/:listing_id/variation-images', uri_params=[ listing_id,], method='POST', query_params=query_params, data=data,)
# EndMethod: updateVariationImages


# StartMethod: findAllListingActive
def findAllListingActive(self, query_params=None):
    return self.requester.make_request(uri='/listings/active', uri_params=[], method='GET', query_params=query_params,)
# EndMethod: findAllListingActive


# StartMethod: getInterestingListings
def getInterestingListings(self, query_params=None):
    return self.requester.make_request(uri='/listings/interesting', uri_params=[], method='GET', query_params=query_params,)
# EndMethod: getInterestingListings


# StartMethod: getTrendingListings
def getTrendingListings(self, query_params=None):
    return self.requester.make_request(uri='/listings/trending', uri_params=[], method='GET', query_params=query_params,)
# EndMethod: getTrendingListings


# StartMethod: pagesSignup
def pagesSignup(self, data=None, query_params=None):
    return self.requester.make_request(uri='/pages-signup', uri_params=[], method='POST', query_params=query_params, data=data,)
# EndMethod: pagesSignup


# StartMethod: findPage
def findPage(self, page_id, query_params=None):
    return self.requester.make_request(uri='/pages/:page_id', uri_params=[ page_id,], method='GET', query_params=query_params,)
# EndMethod: findPage


# StartMethod: updatePageData
def updatePageData(self, page_id, data=None, query_params=None):
    return self.requester.make_request(uri='/pages/:page_id', uri_params=[ page_id,], method='POST', query_params=query_params, data=data,)
# EndMethod: updatePageData


# StartMethod: uploadAvatar
def uploadAvatar(self, user_id, data=None, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/users/:user_id/avatar', uri_params=[ user_id,], method='POST', query_params=query_params, data=data,)
# EndMethod: uploadAvatar


# StartMethod: findAllPageCollections
def findAllPageCollections(self, page_id, query_params=None):
    return self.requester.make_request(uri='/pages/:page_id/collections', uri_params=[ page_id,], method='GET', query_params=query_params,)
# EndMethod: findAllPageCollections


# StartMethod: createPageCollection
def createPageCollection(self, page_id, data=None, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/pages/:page_id/collections', uri_params=[ page_id,], method='POST', query_params=query_params, data=data,)
# EndMethod: createPageCollection


# StartMethod: getPageCollection
def getPageCollection(self, page_id, collection_id, query_params=None):
    return self.requester.make_request(uri='/pages/:page_id/collections/:collection_id', uri_params=[ page_id, collection_id,], method='GET', query_params=query_params,)
# EndMethod: getPageCollection


# StartMethod: updatePageCollection
def updatePageCollection(self, page_id, collection_id, data=None, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/pages/:page_id/collections/:collection_id', uri_params=[ page_id, collection_id,], method='PUT', query_params=query_params, data=data,)
# EndMethod: updatePageCollection


# StartMethod: deletePageCollection
def deletePageCollection(self, page_id, collection_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/pages/:page_id/collections/:collection_id', uri_params=[ page_id, collection_id,], method='DELETE', query_params=query_params,)
# EndMethod: deletePageCollection


# StartMethod: getCollectionListings
def getCollectionListings(self, page_id, collection_id, query_params=None):
    return self.requester.make_request(uri='/pages/:page_id/collections/:collection_id/listings', uri_params=[ page_id, collection_id,], method='GET', query_params=query_params,)
# EndMethod: getCollectionListings


# StartMethod: addListingToCollection
def addListingToCollection(self, page_id, collection_id, listing_id, data=None, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/pages/:page_id/collections/:collection_id/listings/:listing_id', uri_params=[ page_id, collection_id, listing_id,], method='POST', query_params=query_params, data=data,)
# EndMethod: addListingToCollection


# StartMethod: removeListingFromCollection
def removeListingFromCollection(self, page_id, collection_id, listing_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/pages/:page_id/collections/:collection_id/listings/:listing_id', uri_params=[ page_id, collection_id, listing_id,], method='DELETE', query_params=query_params,)
# EndMethod: removeListingFromCollection


# StartMethod: findPageCollectionsForListings
def findPageCollectionsForListings(self, page_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/pages/:page_id/collections/listings_map', uri_params=[ page_id,], method='GET', query_params=query_params,)
# EndMethod: findPageCollectionsForListings


# StartMethod: addCurator
def addCurator(self, page_id, curator_id, data=None, query_params=None):
    return self.requester.make_request(uri='/pages/:page_id/curators/:curator_id', uri_params=[ page_id, curator_id,], method='POST', query_params=query_params, data=data,)
# EndMethod: addCurator


# StartMethod: removeCurator
def removeCurator(self, page_id, curator_id, query_params=None):
    return self.requester.make_request(uri='/pages/:page_id/curators/:curator_id', uri_params=[ page_id, curator_id,], method='DELETE', query_params=query_params,)
# EndMethod: removeCurator


# StartMethod: curatorPeopleSearch
def curatorPeopleSearch(self, query_params=None):
    return self.requester.make_request(uri='/pages/find-curators', uri_params=[], method='GET', query_params=query_params,)
# EndMethod: curatorPeopleSearch


# StartMethod: findPayment
def findPayment(self, payment_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/payments/:payment_id', uri_params=[ payment_id,], method='GET', query_params=query_params,)
# EndMethod: findPayment


# StartMethod: findPaymentAdjustments
def findPaymentAdjustments(self, payment_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/payments/:payment_id/adjustments', uri_params=[ payment_id,], method='GET', query_params=query_params,)
# EndMethod: findPaymentAdjustments


# StartMethod: findPaymentAdjustment
def findPaymentAdjustment(self, payment_id, payment_adjustment_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/payments/:payment_id/adjustments/:payment_adjustment_id', uri_params=[ payment_id, payment_adjustment_id,], method='GET', query_params=query_params,)
# EndMethod: findPaymentAdjustment


# StartMethod: findPaymentAdjustmentItems
def findPaymentAdjustmentItems(self, payment_id, payment_adjustment_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/payments/:payment_id/adjustments/:payment_adjustment_id/items', uri_params=[ payment_id, payment_adjustment_id,], method='GET', query_params=query_params,)
# EndMethod: findPaymentAdjustmentItems


# StartMethod: findPaymentAdjustmentItem
def findPaymentAdjustmentItem(self, payment_id, payment_adjustment_id, payment_adjustment_item_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/payments/:payment_id/adjustments/:payment_adjustment_id/items/:payment_adjustment_item_id', uri_params=[ payment_id, payment_adjustment_id, payment_adjustment_item_id,], method='GET', query_params=query_params,)
# EndMethod: findPaymentAdjustmentItem


# StartMethod: getPrivateBaseline
def getPrivateBaseline(self, query_params=None):
    return self.requester.make_request(uri='/private-baseline', uri_params=[], method='GET', query_params=query_params,)
# EndMethod: getPrivateBaseline


# StartMethod: getPropertyOptionModifier
def getPropertyOptionModifier(self, query_params=None):
    return self.requester.make_request(uri='/property_options/modifiers', uri_params=[], method='GET', query_params=query_params,)
# EndMethod: getPropertyOptionModifier


# StartMethod: findAllSuggestedPropertyOptions
def findAllSuggestedPropertyOptions(self, query_params=None):
    return self.requester.make_request(uri='/property_options/suggested', uri_params=[], method='GET', query_params=query_params,)
# EndMethod: findAllSuggestedPropertyOptions


# StartMethod: findPropertySet
def findPropertySet(self, query_params=None):
    return self.requester.make_request(uri='/property_sets', uri_params=[], method='GET', query_params=query_params,)
# EndMethod: findPropertySet


# StartMethod: getShop_Receipt2
def getShop_Receipt2(self, receipt_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/receipts/:receipt_id', uri_params=[ receipt_id,], method='GET', query_params=query_params,)
# EndMethod: getShop_Receipt2


# StartMethod: updateReceipt
def updateReceipt(self, receipt_id, data=None, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/receipts/:receipt_id', uri_params=[ receipt_id,], method='PUT', query_params=query_params, data=data,)
# EndMethod: updateReceipt


# StartMethod: findAllReceiptListings
def findAllReceiptListings(self, receipt_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/receipts/:receipt_id/listings', uri_params=[ receipt_id,], method='GET', query_params=query_params,)
# EndMethod: findAllReceiptListings


# StartMethod: findAllShop_Receipt2Transactions
def findAllShop_Receipt2Transactions(self, receipt_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/receipts/:receipt_id/transactions', uri_params=[ receipt_id,], method='GET', query_params=query_params,)
# EndMethod: findAllShop_Receipt2Transactions


# StartMethod: findAllRegion
def findAllRegion(self, query_params=None):
    return self.requester.make_request(uri='/regions', uri_params=[], method='GET', query_params=query_params,)
# EndMethod: findAllRegion


# StartMethod: getRegion
def getRegion(self, region_id, query_params=None):
    return self.requester.make_request(uri='/regions/:region_id', uri_params=[ region_id,], method='GET', query_params=query_params,)
# EndMethod: getRegion


# StartMethod: findEligibleRegions
def findEligibleRegions(self, query_params=None):
    return self.requester.make_request(uri='/regions/eligible', uri_params=[], method='GET', query_params=query_params,)
# EndMethod: findEligibleRegions


# StartMethod: getServerEpoch
def getServerEpoch(self, query_params=None):
    return self.requester.make_request(uri='/server/epoch', uri_params=[], method='GET', query_params=query_params,)
# EndMethod: getServerEpoch


# StartMethod: ping
def ping(self, query_params=None):
    return self.requester.make_request(uri='/server/ping', uri_params=[], method='GET', query_params=query_params,)
# EndMethod: ping


# StartMethod: getShippingCosts
def getShippingCosts(self, shipping_provider_id, data=None, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/shipping/:shipping_provider_id/postage-costs', uri_params=[ shipping_provider_id,], method='POST', query_params=query_params, data=data,)
# EndMethod: getShippingCosts


# StartMethod: getShippingInfo
def getShippingInfo(self, shipping_info_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/shipping/info/:shipping_info_id', uri_params=[ shipping_info_id,], method='GET', query_params=query_params,)
# EndMethod: getShippingInfo


# StartMethod: updateShippingInfo
def updateShippingInfo(self, shipping_info_id, data=None, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/shipping/info/:shipping_info_id', uri_params=[ shipping_info_id,], method='PUT', query_params=query_params, data=data,)
# EndMethod: updateShippingInfo


# StartMethod: deleteShippingInfo
def deleteShippingInfo(self, shipping_info_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/shipping/info/:shipping_info_id', uri_params=[ shipping_info_id,], method='DELETE', query_params=query_params,)
# EndMethod: deleteShippingInfo


# StartMethod: getPostageRates
def getPostageRates(self, shipping_provider_id, data=None, query_params=None):
    return self.requester.make_request(uri='/shipping/providers/:shipping_provider_id/mail-class-rates', uri_params=[ shipping_provider_id,], method='POST', query_params=query_params, data=data,)
# EndMethod: getPostageRates


# StartMethod: createShippingTemplate
def createShippingTemplate(self, data=None, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/shipping/templates', uri_params=[], method='POST', query_params=query_params, data=data,)
# EndMethod: createShippingTemplate


# StartMethod: getShippingTemplate
def getShippingTemplate(self, shipping_template_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/shipping/templates/:shipping_template_id', uri_params=[ shipping_template_id,], method='GET', query_params=query_params,)
# EndMethod: getShippingTemplate


# StartMethod: updateShippingTemplate
def updateShippingTemplate(self, shipping_template_id, data=None, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/shipping/templates/:shipping_template_id', uri_params=[ shipping_template_id,], method='PUT', query_params=query_params, data=data,)
# EndMethod: updateShippingTemplate


# StartMethod: deleteShippingTemplate
def deleteShippingTemplate(self, shipping_template_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/shipping/templates/:shipping_template_id', uri_params=[ shipping_template_id,], method='DELETE', query_params=query_params,)
# EndMethod: deleteShippingTemplate


# StartMethod: findAllShippingTemplateEntries
def findAllShippingTemplateEntries(self, shipping_template_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/shipping/templates/:shipping_template_id/entries', uri_params=[ shipping_template_id,], method='GET', query_params=query_params,)
# EndMethod: findAllShippingTemplateEntries


# StartMethod: findAllShippingTemplateUpgrades
def findAllShippingTemplateUpgrades(self, shipping_template_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/shipping/templates/:shipping_template_id/upgrades', uri_params=[ shipping_template_id,], method='GET', query_params=query_params,)
# EndMethod: findAllShippingTemplateUpgrades


# StartMethod: createShippingTemplateUpgrade
def createShippingTemplateUpgrade(self, shipping_template_id, data=None, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/shipping/templates/:shipping_template_id/upgrades', uri_params=[ shipping_template_id,], method='POST', query_params=query_params, data=data,)
# EndMethod: createShippingTemplateUpgrade


# StartMethod: updateShippingTemplateUpgrade
def updateShippingTemplateUpgrade(self, shipping_template_id, data=None, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/shipping/templates/:shipping_template_id/upgrades', uri_params=[ shipping_template_id,], method='PUT', query_params=query_params, data=data,)
# EndMethod: updateShippingTemplateUpgrade


# StartMethod: deleteShippingTemplateUpgrade
def deleteShippingTemplateUpgrade(self, shipping_template_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/shipping/templates/:shipping_template_id/upgrades', uri_params=[ shipping_template_id,], method='DELETE', query_params=query_params,)
# EndMethod: deleteShippingTemplateUpgrade


# StartMethod: createShippingTemplateEntry
def createShippingTemplateEntry(self, data=None, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/shipping/templates/entries', uri_params=[], method='POST', query_params=query_params, data=data,)
# EndMethod: createShippingTemplateEntry


# StartMethod: getShippingTemplateEntry
def getShippingTemplateEntry(self, shipping_template_entry_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/shipping/templates/entries/:shipping_template_entry_id', uri_params=[ shipping_template_entry_id,], method='GET', query_params=query_params,)
# EndMethod: getShippingTemplateEntry


# StartMethod: updateShippingTemplateEntry
def updateShippingTemplateEntry(self, shipping_template_entry_id, data=None, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/shipping/templates/entries/:shipping_template_entry_id', uri_params=[ shipping_template_entry_id,], method='PUT', query_params=query_params, data=data,)
# EndMethod: updateShippingTemplateEntry


# StartMethod: deleteShippingTemplateEntry
def deleteShippingTemplateEntry(self, shipping_template_entry_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/shipping/templates/entries/:shipping_template_entry_id', uri_params=[ shipping_template_entry_id,], method='DELETE', query_params=query_params,)
# EndMethod: deleteShippingTemplateEntry


# StartMethod: findAllShops
def findAllShops(self, query_params=None):
    return self.requester.make_request(uri='/shops', uri_params=[], method='GET', query_params=query_params,)
# EndMethod: findAllShops


# StartMethod: getShop
def getShop(self, shop_id, query_params=None):
    return self.requester.make_request(uri='/shops/:shop_id', uri_params=[ shop_id,], method='GET', query_params=query_params,)
# EndMethod: getShop


# StartMethod: updateShop
def updateShop(self, shop_id, data=None, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/shops/:shop_id', uri_params=[ shop_id,], method='PUT', query_params=query_params, data=data,)
# EndMethod: updateShop


# StartMethod: getShopAbout
def getShopAbout(self, shop_id, query_params=None):
    return self.requester.make_request(uri='/shops/:shop_id/about', uri_params=[ shop_id,], method='GET', query_params=query_params,)
# EndMethod: getShopAbout


# StartMethod: uploadShopBanner
def uploadShopBanner(self, shop_id, data=None, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/shops/:shop_id/appearance/banner', uri_params=[ shop_id,], method='POST', query_params=query_params, data=data,)
# EndMethod: uploadShopBanner


# StartMethod: deleteShopBanner
def deleteShopBanner(self, shop_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/shops/:shop_id/appearance/banner', uri_params=[ shop_id,], method='DELETE', query_params=query_params,)
# EndMethod: deleteShopBanner


# StartMethod: findAllShopCoupons
def findAllShopCoupons(self, shop_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/shops/:shop_id/coupons', uri_params=[ shop_id,], method='GET', query_params=query_params,)
# EndMethod: findAllShopCoupons


# StartMethod: createCoupon
def createCoupon(self, shop_id, data=None, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/shops/:shop_id/coupons', uri_params=[ shop_id,], method='POST', query_params=query_params, data=data,)
# EndMethod: createCoupon


# StartMethod: findCoupon
def findCoupon(self, shop_id, coupon_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/shops/:shop_id/coupons/:coupon_id', uri_params=[ shop_id, coupon_id,], method='GET', query_params=query_params,)
# EndMethod: findCoupon


# StartMethod: updateCoupon
def updateCoupon(self, shop_id, coupon_id, data=None, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/shops/:shop_id/coupons/:coupon_id', uri_params=[ shop_id, coupon_id,], method='PUT', query_params=query_params, data=data,)
# EndMethod: updateCoupon


# StartMethod: deleteCoupon
def deleteCoupon(self, shop_id, coupon_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/shops/:shop_id/coupons/:coupon_id', uri_params=[ shop_id, coupon_id,], method='DELETE', query_params=query_params,)
# EndMethod: deleteCoupon


# StartMethod: findLedger
def findLedger(self, shop_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/shops/:shop_id/ledger/', uri_params=[ shop_id,], method='GET', query_params=query_params,)
# EndMethod: findLedger


# StartMethod: findLedgerEntries
def findLedgerEntries(self, shop_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/shops/:shop_id/ledger/entries', uri_params=[ shop_id,], method='GET', query_params=query_params,)
# EndMethod: findLedgerEntries


# StartMethod: findLedgerEntry
def findLedgerEntry(self, shop_id, ledger_entry_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/shops/:shop_id/ledger/entries/:ledger_entry_id', uri_params=[ shop_id, ledger_entry_id,], method='GET', query_params=query_params,)
# EndMethod: findLedgerEntry


# StartMethod: findPaymentAdjustmentForLedgerEntry
def findPaymentAdjustmentForLedgerEntry(self, shop_id, ledger_entry_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/shops/:shop_id/ledger/entries/:ledger_entry_id/adjustment', uri_params=[ shop_id, ledger_entry_id,], method='GET', query_params=query_params,)
# EndMethod: findPaymentAdjustmentForLedgerEntry


# StartMethod: findPaymentForLedgerEntry
def findPaymentForLedgerEntry(self, shop_id, ledger_entry_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/shops/:shop_id/ledger/entries/:ledger_entry_id/payment', uri_params=[ shop_id, ledger_entry_id,], method='GET', query_params=query_params,)
# EndMethod: findPaymentForLedgerEntry


# StartMethod: findAllShopListingsActive
def findAllShopListingsActive(self, shop_id, query_params=None):
    return self.requester.make_request(uri='/shops/:shop_id/listings/active', uri_params=[ shop_id,], method='GET', query_params=query_params,)
# EndMethod: findAllShopListingsActive


# StartMethod: findAllShopListingsDraft
def findAllShopListingsDraft(self, shop_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/shops/:shop_id/listings/draft', uri_params=[ shop_id,], method='GET', query_params=query_params,)
# EndMethod: findAllShopListingsDraft


# StartMethod: findAllShopListingsExpired
def findAllShopListingsExpired(self, shop_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/shops/:shop_id/listings/expired', uri_params=[ shop_id,], method='GET', query_params=query_params,)
# EndMethod: findAllShopListingsExpired


# StartMethod: getShopListingExpired
def getShopListingExpired(self, shop_id, listing_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/shops/:shop_id/listings/expired/:listing_id', uri_params=[ shop_id, listing_id,], method='GET', query_params=query_params,)
# EndMethod: getShopListingExpired


# StartMethod: findAllShopListingsFeatured
def findAllShopListingsFeatured(self, shop_id, query_params=None):
    return self.requester.make_request(uri='/shops/:shop_id/listings/featured', uri_params=[ shop_id,], method='GET', query_params=query_params,)
# EndMethod: findAllShopListingsFeatured


# StartMethod: findAllShopListingsInactive
def findAllShopListingsInactive(self, shop_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/shops/:shop_id/listings/inactive', uri_params=[ shop_id,], method='GET', query_params=query_params,)
# EndMethod: findAllShopListingsInactive


# StartMethod: getShopListingInactive
def getShopListingInactive(self, shop_id, listing_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/shops/:shop_id/listings/inactive/:listing_id', uri_params=[ shop_id, listing_id,], method='GET', query_params=query_params,)
# EndMethod: getShopListingInactive


# StartMethod: findPaymentAccountEntries
def findPaymentAccountEntries(self, shop_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/shops/:shop_id/payment_account/entries', uri_params=[ shop_id,], method='GET', query_params=query_params,)
# EndMethod: findPaymentAccountEntries


# StartMethod: findPaymentAdjustmentForPaymentAccountLedgerEntry
def findPaymentAdjustmentForPaymentAccountLedgerEntry(self, shop_id, ledger_entry_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/shops/:shop_id/payment_account/entries/:ledger_entry_id/adjustment', uri_params=[ shop_id, ledger_entry_id,], method='GET', query_params=query_params,)
# EndMethod: findPaymentAdjustmentForPaymentAccountLedgerEntry


# StartMethod: findPaymentForPaymentAccountLedgerEntry
def findPaymentForPaymentAccountLedgerEntry(self, shop_id, ledger_entry_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/shops/:shop_id/payment_account/entries/:ledger_entry_id/payment', uri_params=[ shop_id, ledger_entry_id,], method='GET', query_params=query_params,)
# EndMethod: findPaymentForPaymentAccountLedgerEntry


# StartMethod: findShopPaymentTemplates
def findShopPaymentTemplates(self, shop_id, query_params=None):
    return self.requester.make_request(uri='/shops/:shop_id/payment_templates', uri_params=[ shop_id,], method='GET', query_params=query_params,)
# EndMethod: findShopPaymentTemplates


# StartMethod: createShopPaymentTemplate
def createShopPaymentTemplate(self, shop_id, data=None, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/shops/:shop_id/payment_templates', uri_params=[ shop_id,], method='POST', query_params=query_params, data=data,)
# EndMethod: createShopPaymentTemplate


# StartMethod: updateShopPaymentTemplate
def updateShopPaymentTemplate(self, shop_id, payment_template_id, data=None, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/shops/:shop_id/payment_templates/:payment_template_id', uri_params=[ shop_id, payment_template_id,], method='PUT', query_params=query_params, data=data,)
# EndMethod: updateShopPaymentTemplate


# StartMethod: findAllShopReceipts
def findAllShopReceipts(self, shop_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/shops/:shop_id/receipts', uri_params=[ shop_id,], method='GET', query_params=query_params,)
# EndMethod: findAllShopReceipts


# StartMethod: findShopPaymentByReceipt
def findShopPaymentByReceipt(self, shop_id, receipt_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/shops/:shop_id/receipts/:receipt_id/payments', uri_params=[ shop_id, receipt_id,], method='GET', query_params=query_params,)
# EndMethod: findShopPaymentByReceipt


# StartMethod: submitTracking
def submitTracking(self, shop_id, receipt_id, data=None, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/shops/:shop_id/receipts/:receipt_id/tracking', uri_params=[ shop_id, receipt_id,], method='POST', query_params=query_params, data=data,)
# EndMethod: submitTracking


# StartMethod: findAllShopReceiptsByStatus
def findAllShopReceiptsByStatus(self, shop_id, status, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/shops/:shop_id/receipts/:status', uri_params=[ shop_id, status,], method='GET', query_params=query_params,)
# EndMethod: findAllShopReceiptsByStatus


# StartMethod: searchAllShopReceipts
def searchAllShopReceipts(self, shop_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/shops/:shop_id/receipts/search', uri_params=[ shop_id,], method='GET', query_params=query_params,)
# EndMethod: searchAllShopReceipts


# StartMethod: getShopReviews
def getShopReviews(self, shop_id, query_params=None):
    return self.requester.make_request(uri='/shops/:shop_id/reviews', uri_params=[ shop_id,], method='GET', query_params=query_params,)
# EndMethod: getShopReviews


# StartMethod: findAllShopSections
def findAllShopSections(self, shop_id, query_params=None):
    return self.requester.make_request(uri='/shops/:shop_id/sections', uri_params=[ shop_id,], method='GET', query_params=query_params,)
# EndMethod: findAllShopSections


# StartMethod: createShopSection
def createShopSection(self, shop_id, data=None, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/shops/:shop_id/sections', uri_params=[ shop_id,], method='POST', query_params=query_params, data=data,)
# EndMethod: createShopSection


# StartMethod: getShopSection
def getShopSection(self, shop_id, shop_section_id, query_params=None):
    return self.requester.make_request(uri='/shops/:shop_id/sections/:shop_section_id', uri_params=[ shop_id, shop_section_id,], method='GET', query_params=query_params,)
# EndMethod: getShopSection


# StartMethod: updateShopSection
def updateShopSection(self, shop_id, shop_section_id, data=None, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/shops/:shop_id/sections/:shop_section_id', uri_params=[ shop_id, shop_section_id,], method='PUT', query_params=query_params, data=data,)
# EndMethod: updateShopSection


# StartMethod: deleteShopSection
def deleteShopSection(self, shop_id, shop_section_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/shops/:shop_id/sections/:shop_section_id', uri_params=[ shop_id, shop_section_id,], method='DELETE', query_params=query_params,)
# EndMethod: deleteShopSection


# StartMethod: findAllShopSectionListings
def findAllShopSectionListings(self, shop_id, shop_section_id, query_params=None):
    return self.requester.make_request(uri='/shops/:shop_id/sections/:shop_section_id/listings', uri_params=[ shop_id, shop_section_id,], method='GET', query_params=query_params,)
# EndMethod: findAllShopSectionListings


# StartMethod: findAllShopSectionListingsActive
def findAllShopSectionListingsActive(self, shop_id, shop_section_id, query_params=None):
    return self.requester.make_request(uri='/shops/:shop_id/sections/:shop_section_id/listings/active', uri_params=[ shop_id, shop_section_id,], method='GET', query_params=query_params,)
# EndMethod: findAllShopSectionListingsActive


# StartMethod: getShopSectionTranslation
def getShopSectionTranslation(self, shop_id, shop_section_id, language, query_params=None):
    return self.requester.make_request(uri='/shops/:shop_id/sections/:shop_section_id/translations/:language', uri_params=[ shop_id, shop_section_id, language,], method='GET', query_params=query_params,)
# EndMethod: getShopSectionTranslation


# StartMethod: createShopSectionTranslation
def createShopSectionTranslation(self, shop_id, shop_section_id, language, data=None, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/shops/:shop_id/sections/:shop_section_id/translations/:language', uri_params=[ shop_id, shop_section_id, language,], method='POST', query_params=query_params, data=data,)
# EndMethod: createShopSectionTranslation


# StartMethod: updateShopSectionTranslation
def updateShopSectionTranslation(self, shop_id, shop_section_id, language, data=None, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/shops/:shop_id/sections/:shop_section_id/translations/:language', uri_params=[ shop_id, shop_section_id, language,], method='PUT', query_params=query_params, data=data,)
# EndMethod: updateShopSectionTranslation


# StartMethod: deleteShopSectionTranslation
def deleteShopSectionTranslation(self, shop_id, shop_section_id, language, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/shops/:shop_id/sections/:shop_section_id/translations/:language', uri_params=[ shop_id, shop_section_id, language,], method='DELETE', query_params=query_params,)
# EndMethod: deleteShopSectionTranslation


# StartMethod: findAllShopTransactions
def findAllShopTransactions(self, shop_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/shops/:shop_id/transactions', uri_params=[ shop_id,], method='GET', query_params=query_params,)
# EndMethod: findAllShopTransactions


# StartMethod: getShopTranslation
def getShopTranslation(self, shop_id, language, query_params=None):
    return self.requester.make_request(uri='/shops/:shop_id/translations/:language', uri_params=[ shop_id, language,], method='GET', query_params=query_params,)
# EndMethod: getShopTranslation


# StartMethod: createShopTranslation
def createShopTranslation(self, shop_id, language, data=None, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/shops/:shop_id/translations/:language', uri_params=[ shop_id, language,], method='POST', query_params=query_params, data=data,)
# EndMethod: createShopTranslation


# StartMethod: updateShopTranslation
def updateShopTranslation(self, shop_id, language, data=None, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/shops/:shop_id/translations/:language', uri_params=[ shop_id, language,], method='PUT', query_params=query_params, data=data,)
# EndMethod: updateShopTranslation


# StartMethod: deleteShopTranslation
def deleteShopTranslation(self, shop_id, language, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/shops/:shop_id/translations/:language', uri_params=[ shop_id, language,], method='DELETE', query_params=query_params,)
# EndMethod: deleteShopTranslation


# StartMethod: getListingShop
def getListingShop(self, listing_id, query_params=None):
    return self.requester.make_request(uri='/shops/listing/:listing_id', uri_params=[ listing_id,], method='GET', query_params=query_params,)
# EndMethod: getListingShop


# StartMethod: getBuyerTaxonomy
def getBuyerTaxonomy(self, query_params=None):
    return self.requester.make_request(uri='/taxonomy/buyer/get', uri_params=[], method='GET', query_params=query_params,)
# EndMethod: getBuyerTaxonomy


# StartMethod: getTaxonomyNodeProperties
def getTaxonomyNodeProperties(self, taxonomy_id, query_params=None):
    return self.requester.make_request(uri='/taxonomy/seller/:taxonomy_id/properties', uri_params=[ taxonomy_id,], method='GET', query_params=query_params,)
# EndMethod: getTaxonomyNodeProperties


# StartMethod: getSellerTaxonomy
def getSellerTaxonomy(self, query_params=None):
    return self.requester.make_request(uri='/taxonomy/seller/get', uri_params=[], method='GET', query_params=query_params,)
# EndMethod: getSellerTaxonomy


# StartMethod: getSellerTaxonomyVersion
def getSellerTaxonomyVersion(self, query_params=None):
    return self.requester.make_request(uri='/taxonomy/seller/version', uri_params=[], method='GET', query_params=query_params,)
# EndMethod: getSellerTaxonomyVersion


# StartMethod: findSuggestedStyles
def findSuggestedStyles(self, query_params=None):
    return self.requester.make_request(uri='/taxonomy/styles', uri_params=[], method='GET', query_params=query_params,)
# EndMethod: findSuggestedStyles


# StartMethod: findAllTeams
def findAllTeams(self, query_params=None):
    return self.requester.make_request(uri='/teams', uri_params=[], method='GET', query_params=query_params,)
# EndMethod: findAllTeams


# StartMethod: findAllUsersForTeam
def findAllUsersForTeam(self, team_id, query_params=None):
    return self.requester.make_request(uri='/teams/:team_id/users/', uri_params=[ team_id,], method='GET', query_params=query_params,)
# EndMethod: findAllUsersForTeam


# StartMethod: findTeams
def findTeams(self, team_ids, query_params=None):
    return self.requester.make_request(uri='/teams/:team_ids/', uri_params=[ team_ids,], method='GET', query_params=query_params,)
# EndMethod: findTeams


# StartMethod: getShop_Transaction
def getShop_Transaction(self, transaction_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/transactions/:transaction_id', uri_params=[ transaction_id,], method='GET', query_params=query_params,)
# EndMethod: getShop_Transaction


# StartMethod: findAllTreasuries
def findAllTreasuries(self, query_params=None):
    return self.requester.make_request(uri='/treasuries', uri_params=[], method='GET', query_params=query_params,)
# EndMethod: findAllTreasuries


# StartMethod: getTreasury
def getTreasury(self, treasury_key, query_params=None):
    return self.requester.make_request(uri='/treasuries/:treasury_key', uri_params=[ treasury_key,], method='GET', query_params=query_params,)
# EndMethod: getTreasury


# StartMethod: deleteTreasury
def deleteTreasury(self, treasury_key, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/treasuries/:treasury_key', uri_params=[ treasury_key,], method='DELETE', query_params=query_params,)
# EndMethod: deleteTreasury


# StartMethod: findTreasuryComments
def findTreasuryComments(self, treasury_key, query_params=None):
    return self.requester.make_request(uri='/treasuries/:treasury_key/comments', uri_params=[ treasury_key,], method='GET', query_params=query_params,)
# EndMethod: findTreasuryComments


# StartMethod: postTreasuryComment
def postTreasuryComment(self, treasury_key, data=None, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/treasuries/:treasury_key/comments', uri_params=[ treasury_key,], method='POST', query_params=query_params, data=data,)
# EndMethod: postTreasuryComment


# StartMethod: deleteTreasuryComment
def deleteTreasuryComment(self, treasury_key, comment_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/treasuries/:treasury_key/comments/:comment_id', uri_params=[ treasury_key, comment_id,], method='DELETE', query_params=query_params,)
# EndMethod: deleteTreasuryComment


# StartMethod: addTreasuryListing
def addTreasuryListing(self, treasury_key, data=None, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/treasuries/:treasury_key/listings', uri_params=[ treasury_key,], method='POST', query_params=query_params, data=data,)
# EndMethod: addTreasuryListing


# StartMethod: removeTreasuryListing
def removeTreasuryListing(self, treasury_key, listing_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/treasuries/:treasury_key/listings/:listing_id', uri_params=[ treasury_key, listing_id,], method='DELETE', query_params=query_params,)
# EndMethod: removeTreasuryListing


# StartMethod: describeOccasionEnum
def describeOccasionEnum(self, query_params=None):
    return self.requester.make_request(uri='/types/enum/occasion', uri_params=[], method='GET', query_params=query_params,)
# EndMethod: describeOccasionEnum


# StartMethod: describeRecipientEnum
def describeRecipientEnum(self, query_params=None):
    return self.requester.make_request(uri='/types/enum/recipient', uri_params=[], method='GET', query_params=query_params,)
# EndMethod: describeRecipientEnum


# StartMethod: describeWhenMadeEnum
def describeWhenMadeEnum(self, query_params=None):
    return self.requester.make_request(uri='/types/enum/when_made', uri_params=[], method='GET', query_params=query_params,)
# EndMethod: describeWhenMadeEnum


# StartMethod: describeWhoMadeEnum
def describeWhoMadeEnum(self, query_params=None):
    return self.requester.make_request(uri='/types/enum/who_made', uri_params=[], method='GET', query_params=query_params,)
# EndMethod: describeWhoMadeEnum


# StartMethod: findAllUsers
def findAllUsers(self, query_params=None):
    return self.requester.make_request(uri='/users', uri_params=[], method='GET', query_params=query_params,)
# EndMethod: findAllUsers


# StartMethod: getUser
def getUser(self, user_id, query_params=None):
    return self.requester.make_request(uri='/users/:user_id', uri_params=[ user_id,], method='GET', query_params=query_params,)
# EndMethod: getUser


# StartMethod: findAllUserAddresses
def findAllUserAddresses(self, user_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/users/:user_id/addresses', uri_params=[ user_id,], method='GET', query_params=query_params,)
# EndMethod: findAllUserAddresses


# StartMethod: createUserAddress
def createUserAddress(self, user_id, data=None, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/users/:user_id/addresses/', uri_params=[ user_id,], method='POST', query_params=query_params, data=data,)
# EndMethod: createUserAddress


# StartMethod: getUserAddress
def getUserAddress(self, user_id, user_address_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/users/:user_id/addresses/:user_address_id', uri_params=[ user_id, user_address_id,], method='GET', query_params=query_params,)
# EndMethod: getUserAddress


# StartMethod: deleteUserAddress
def deleteUserAddress(self, user_id, user_address_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/users/:user_id/addresses/:user_address_id', uri_params=[ user_id, user_address_id,], method='DELETE', query_params=query_params,)
# EndMethod: deleteUserAddress


# StartMethod: getAvatarImgSrc
def getAvatarImgSrc(self, user_id, query_params=None):
    return self.requester.make_request(uri='/users/:user_id/avatar/src', uri_params=[ user_id,], method='GET', query_params=query_params,)
# EndMethod: getAvatarImgSrc


# StartMethod: getUserBillingOverview
def getUserBillingOverview(self, user_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/users/:user_id/billing/overview', uri_params=[ user_id,], method='GET', query_params=query_params,)
# EndMethod: getUserBillingOverview


# StartMethod: getAllUserCarts
def getAllUserCarts(self, user_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/users/:user_id/carts', uri_params=[ user_id,], method='GET', query_params=query_params,)
# EndMethod: getAllUserCarts


# StartMethod: addToCart
def addToCart(self, user_id, data=None, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/users/:user_id/carts', uri_params=[ user_id,], method='POST', query_params=query_params, data=data,)
# EndMethod: addToCart


# StartMethod: updateCartListingQuantity
def updateCartListingQuantity(self, user_id, data=None, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/users/:user_id/carts', uri_params=[ user_id,], method='PUT', query_params=query_params, data=data,)
# EndMethod: updateCartListingQuantity


# StartMethod: removeCartListing
def removeCartListing(self, user_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/users/:user_id/carts', uri_params=[ user_id,], method='DELETE', query_params=query_params,)
# EndMethod: removeCartListing


# StartMethod: getUserCart
def getUserCart(self, user_id, cart_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/users/:user_id/carts/:cart_id', uri_params=[ user_id, cart_id,], method='GET', query_params=query_params,)
# EndMethod: getUserCart


# StartMethod: updateCart
def updateCart(self, user_id, cart_id, data=None, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/users/:user_id/carts/:cart_id', uri_params=[ user_id, cart_id,], method='PUT', query_params=query_params, data=data,)
# EndMethod: updateCart


# StartMethod: deleteCart
def deleteCart(self, user_id, cart_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/users/:user_id/carts/:cart_id', uri_params=[ user_id, cart_id,], method='DELETE', query_params=query_params,)
# EndMethod: deleteCart


# StartMethod: addAndSelectShippingForApplePay
def addAndSelectShippingForApplePay(self, user_id, cart_id, data=None, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/users/:user_id/carts/:cart_id/add_and_select_shipping_for_apple', uri_params=[ user_id, cart_id,], method='POST', query_params=query_params, data=data,)
# EndMethod: addAndSelectShippingForApplePay


# StartMethod: findAllCartListings
def findAllCartListings(self, user_id, cart_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/users/:user_id/carts/:cart_id/listings', uri_params=[ user_id, cart_id,], method='GET', query_params=query_params,)
# EndMethod: findAllCartListings


# StartMethod: saveListingForLater
def saveListingForLater(self, user_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/users/:user_id/carts/save', uri_params=[ user_id,], method='DELETE', query_params=query_params,)
# EndMethod: saveListingForLater


# StartMethod: getUserCartForShop
def getUserCartForShop(self, user_id, shop_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/users/:user_id/carts/shop/:shop_id', uri_params=[ user_id, shop_id,], method='GET', query_params=query_params,)
# EndMethod: getUserCartForShop


# StartMethod: createSingleListingCart
def createSingleListingCart(self, user_id, data=None, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/users/:user_id/carts/single_listing', uri_params=[ user_id,], method='POST', query_params=query_params, data=data,)
# EndMethod: createSingleListingCart


# StartMethod: findAllUserCharges
def findAllUserCharges(self, user_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/users/:user_id/charges', uri_params=[ user_id,], method='GET', query_params=query_params,)
# EndMethod: findAllUserCharges


# StartMethod: getUserChargesMetadata
def getUserChargesMetadata(self, user_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/users/:user_id/charges/meta', uri_params=[ user_id,], method='GET', query_params=query_params,)
# EndMethod: getUserChargesMetadata


# StartMethod: getCirclesContainingUser
def getCirclesContainingUser(self, user_id, query_params=None):
    return self.requester.make_request(uri='/users/:user_id/circles', uri_params=[ user_id,], method='GET', query_params=query_params,)
# EndMethod: getCirclesContainingUser


# StartMethod: getConnectedUser
def getConnectedUser(self, user_id, to_user_id, query_params=None):
    return self.requester.make_request(uri='/users/:user_id/circles/:to_user_id', uri_params=[ user_id, to_user_id,], method='GET', query_params=query_params,)
# EndMethod: getConnectedUser


# StartMethod: unconnectUsers
def unconnectUsers(self, user_id, to_user_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/users/:user_id/circles/:to_user_id', uri_params=[ user_id, to_user_id,], method='DELETE', query_params=query_params,)
# EndMethod: unconnectUsers


# StartMethod: listFollowingPages
def listFollowingPages(self, user_id, query_params=None):
    return self.requester.make_request(uri='/users/:user_id/connected_pages', uri_params=[ user_id,], method='GET', query_params=query_params,)
# EndMethod: listFollowingPages


# StartMethod: followPage
def followPage(self, user_id, data=None, query_params=None):
    return self.requester.make_request(uri='/users/:user_id/connected_pages', uri_params=[ user_id,], method='POST', query_params=query_params, data=data,)
# EndMethod: followPage


# StartMethod: unfollowPage
def unfollowPage(self, user_id, page_id, query_params=None):
    return self.requester.make_request(uri='/users/:user_id/connected_pages/:page_id', uri_params=[ user_id, page_id,], method='DELETE', query_params=query_params,)
# EndMethod: unfollowPage


# StartMethod: getConnectedUsers
def getConnectedUsers(self, user_id, query_params=None):
    return self.requester.make_request(uri='/users/:user_id/connected_users', uri_params=[ user_id,], method='GET', query_params=query_params,)
# EndMethod: getConnectedUsers


# StartMethod: connectUsers
def connectUsers(self, user_id, data=None, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/users/:user_id/connected_users', uri_params=[ user_id,], method='POST', query_params=query_params, data=data,)
# EndMethod: connectUsers


# StartMethod: findAllUserFavoredBy
def findAllUserFavoredBy(self, user_id, query_params=None):
    return self.requester.make_request(uri='/users/:user_id/favored-by', uri_params=[ user_id,], method='GET', query_params=query_params,)
# EndMethod: findAllUserFavoredBy


# StartMethod: findAllUserFavoriteListings
def findAllUserFavoriteListings(self, user_id, query_params=None):
    return self.requester.make_request(uri='/users/:user_id/favorites/listings', uri_params=[ user_id,], method='GET', query_params=query_params,)
# EndMethod: findAllUserFavoriteListings


# StartMethod: findUserFavoriteListings
def findUserFavoriteListings(self, user_id, listing_id, query_params=None):
    return self.requester.make_request(uri='/users/:user_id/favorites/listings/:listing_id', uri_params=[ user_id, listing_id,], method='GET', query_params=query_params,)
# EndMethod: findUserFavoriteListings


# StartMethod: createUserFavoriteListings
def createUserFavoriteListings(self, user_id, listing_id, data=None, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/users/:user_id/favorites/listings/:listing_id', uri_params=[ user_id, listing_id,], method='POST', query_params=query_params, data=data,)
# EndMethod: createUserFavoriteListings


# StartMethod: deleteUserFavoriteListings
def deleteUserFavoriteListings(self, user_id, listing_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/users/:user_id/favorites/listings/:listing_id', uri_params=[ user_id, listing_id,], method='DELETE', query_params=query_params,)
# EndMethod: deleteUserFavoriteListings


# StartMethod: findAllUserFavoriteUsers
def findAllUserFavoriteUsers(self, user_id, query_params=None):
    return self.requester.make_request(uri='/users/:user_id/favorites/users', uri_params=[ user_id,], method='GET', query_params=query_params,)
# EndMethod: findAllUserFavoriteUsers


# StartMethod: findUserFavoriteUsers
def findUserFavoriteUsers(self, user_id, target_user_id, query_params=None):
    return self.requester.make_request(uri='/users/:user_id/favorites/users/:target_user_id', uri_params=[ user_id, target_user_id,], method='GET', query_params=query_params,)
# EndMethod: findUserFavoriteUsers


# StartMethod: createUserFavoriteUsers
def createUserFavoriteUsers(self, user_id, target_user_id, data=None, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/users/:user_id/favorites/users/:target_user_id', uri_params=[ user_id, target_user_id,], method='POST', query_params=query_params, data=data,)
# EndMethod: createUserFavoriteUsers


# StartMethod: deleteUserFavoriteUsers
def deleteUserFavoriteUsers(self, user_id, target_user_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/users/:user_id/favorites/users/:target_user_id', uri_params=[ user_id, target_user_id,], method='DELETE', query_params=query_params,)
# EndMethod: deleteUserFavoriteUsers


# StartMethod: findAllUserFeedbackAsAuthor
def findAllUserFeedbackAsAuthor(self, user_id, query_params=None):
    return self.requester.make_request(uri='/users/:user_id/feedback/as-author', uri_params=[ user_id,], method='GET', query_params=query_params,)
# EndMethod: findAllUserFeedbackAsAuthor


# StartMethod: findAllUserFeedbackAsBuyer
def findAllUserFeedbackAsBuyer(self, user_id, query_params=None):
    return self.requester.make_request(uri='/users/:user_id/feedback/as-buyer', uri_params=[ user_id,], method='GET', query_params=query_params,)
# EndMethod: findAllUserFeedbackAsBuyer


# StartMethod: findAllUserFeedbackAsSeller
def findAllUserFeedbackAsSeller(self, user_id, query_params=None):
    return self.requester.make_request(uri='/users/:user_id/feedback/as-seller', uri_params=[ user_id,], method='GET', query_params=query_params,)
# EndMethod: findAllUserFeedbackAsSeller


# StartMethod: findAllUserFeedbackAsSubject
def findAllUserFeedbackAsSubject(self, user_id, query_params=None):
    return self.requester.make_request(uri='/users/:user_id/feedback/as-subject', uri_params=[ user_id,], method='GET', query_params=query_params,)
# EndMethod: findAllUserFeedbackAsSubject


# StartMethod: findAllFeedbackFromBuyers
def findAllFeedbackFromBuyers(self, user_id, query_params=None):
    return self.requester.make_request(uri='/users/:user_id/feedback/from-buyers', uri_params=[ user_id,], method='GET', query_params=query_params,)
# EndMethod: findAllFeedbackFromBuyers


# StartMethod: findAllFeedbackFromSellers
def findAllFeedbackFromSellers(self, user_id, query_params=None):
    return self.requester.make_request(uri='/users/:user_id/feedback/from-sellers', uri_params=[ user_id,], method='GET', query_params=query_params,)
# EndMethod: findAllFeedbackFromSellers


# StartMethod: findAllUserPayments
def findAllUserPayments(self, user_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/users/:user_id/payments', uri_params=[ user_id,], method='GET', query_params=query_params,)
# EndMethod: findAllUserPayments


# StartMethod: findAllUserPaymentTemplates
def findAllUserPaymentTemplates(self, user_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/users/:user_id/payments/templates', uri_params=[ user_id,], method='GET', query_params=query_params,)
# EndMethod: findAllUserPaymentTemplates


# StartMethod: findUserProfile
def findUserProfile(self, user_id, query_params=None):
    return self.requester.make_request(uri='/users/:user_id/profile', uri_params=[ user_id,], method='GET', query_params=query_params,)
# EndMethod: findUserProfile


# StartMethod: updateUserProfile
def updateUserProfile(self, user_id, data=None, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/users/:user_id/profile', uri_params=[ user_id,], method='PUT', query_params=query_params, data=data,)
# EndMethod: updateUserProfile


# StartMethod: findAllUserBuyerReceipts
def findAllUserBuyerReceipts(self, user_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/users/:user_id/receipts', uri_params=[ user_id,], method='GET', query_params=query_params,)
# EndMethod: findAllUserBuyerReceipts


# StartMethod: findAllUserShippingProfiles
def findAllUserShippingProfiles(self, user_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/users/:user_id/shipping/templates', uri_params=[ user_id,], method='GET', query_params=query_params,)
# EndMethod: findAllUserShippingProfiles


# StartMethod: findAllUserShops
def findAllUserShops(self, user_id, query_params=None):
    return self.requester.make_request(uri='/users/:user_id/shops', uri_params=[ user_id,], method='GET', query_params=query_params,)
# EndMethod: findAllUserShops


# StartMethod: findAllTeamsForUser
def findAllTeamsForUser(self, user_id, query_params=None):
    return self.requester.make_request(uri='/users/:user_id/teams', uri_params=[ user_id,], method='GET', query_params=query_params,)
# EndMethod: findAllTeamsForUser


# StartMethod: findAllUserBuyerTransactions
def findAllUserBuyerTransactions(self, user_id, query_params=None):
    if self.requester.auth_mode == 'api_key':
        raise RequiresOauth
    return self.requester.make_request(uri='/users/:user_id/transactions', uri_params=[ user_id,], method='GET', query_params=query_params,)
# EndMethod: findAllUserBuyerTransactions


# StartMethod: findAllUserTreasuries
def findAllUserTreasuries(self, user_id, query_params=None):
    return self.requester.make_request(uri='/users/:user_id/treasuries', uri_params=[ user_id,], method='GET', query_params=query_params,)
# EndMethod: findAllUserTreasuries

