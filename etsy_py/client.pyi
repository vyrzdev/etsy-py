from . import rq
import typing

class EtsyClient:
    def __init__(self, requester: rq.EtsyRequester, api_base_url: str = ..., debug: bool = ...) -> EtsyClient:  ...

    # Autogenerated Stubs...

    def getMethodTable(self, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def getPublicBaseline(self, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findAllCountry(self, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def getCountry(self, country_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findByIsoCode(self, iso_code, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findAllFeaturedTreasuries(self, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def getFeaturedTreasuryById(self, featured_treasury_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findAllListingsForFeaturedTreasuryId(self, featured_treasury_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findAllActiveListingsForFeaturedTreasuryId(self, featured_treasury_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findAllFeaturedListings(self, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findAllCurrentFeaturedListings(self, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findAllFeaturedTreasuriesByOwner(self, owner_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def getGuest(self, guest_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findAllGuestCarts(self, guest_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def addToGuestCart(self, guest_id, data: typing.Union[None, dict] = ..., query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def updateGuestCartListingQuantity(self, guest_id, data: typing.Union[None, dict] = ..., query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def removeGuestCartListing(self, guest_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findGuestCart(self, guest_id, cart_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def updateGuestCart(self, guest_id, cart_id, data: typing.Union[None, dict] = ..., query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def deleteGuestCart(self, guest_id, cart_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def claimGuest(self, guest_id, data: typing.Union[None, dict] = ..., query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def mergeGuest(self, guest_id, data: typing.Union[None, dict] = ..., query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def generateGuest(self, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def listImageTypes(self, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def createListing(self, data: typing.Union[None, dict] = ..., query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def getListing(self, listing_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def updateListing(self, listing_id, data: typing.Union[None, dict] = ..., query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def deleteListing(self, listing_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def getAttributes(self, listing_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def getAttribute(self, listing_id, property_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def updateAttribute(self, listing_id, property_id, data: typing.Union[None, dict] = ..., query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def deleteAttribute(self, listing_id, property_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findAllListingFavoredBy(self, listing_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findAllListingFiles(self, listing_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def uploadListingFile(self, listing_id, data: typing.Union[None, dict] = ..., query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findListingFile(self, listing_id, listing_file_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def deleteListingFile(self, listing_id, listing_file_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findAllListingImages(self, listing_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def uploadListingImage(self, listing_id, data: typing.Union[None, dict] = ..., query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def getImage_Listing(self, listing_id, listing_image_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def deleteListingImage(self, listing_id, listing_image_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def getInventory(self, listing_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def updateInventory(self, listing_id, data: typing.Union[None, dict] = ..., query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def getProduct(self, listing_id, product_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def getOffering(self, listing_id, product_id, offering_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findAllListingShippingProfileEntries(self, listing_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def createShippingInfo(self, listing_id, data: typing.Union[None, dict] = ..., query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def getListingShippingUpgrades(self, listing_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def createListingShippingUpgrade(self, listing_id, data: typing.Union[None, dict] = ..., query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def updateListingShippingUpgrade(self, listing_id, data: typing.Union[None, dict] = ..., query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def deleteListingShippingUpgrade(self, listing_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findAllListingTransactions(self, listing_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def getListingTranslation(self, listing_id, language, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def createListingTranslation(self, listing_id, language, data: typing.Union[None, dict] = ..., query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def updateListingTranslation(self, listing_id, language, data: typing.Union[None, dict] = ..., query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def deleteListingTranslation(self, listing_id, language, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def getVariationImages(self, listing_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def updateVariationImages(self, listing_id, data: typing.Union[None, dict] = ..., query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findAllListingActive(self, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def getInterestingListings(self, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def getTrendingListings(self, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def pagesSignup(self, data: typing.Union[None, dict] = ..., query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findPage(self, page_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def updatePageData(self, page_id, data: typing.Union[None, dict] = ..., query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def uploadAvatar(self, page_id, data: typing.Union[None, dict] = ..., query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findAllPageCollections(self, page_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def createPageCollection(self, page_id, data: typing.Union[None, dict] = ..., query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def getPageCollection(self, page_id, collection_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def updatePageCollection(self, page_id, collection_id, data: typing.Union[None, dict] = ..., query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def deletePageCollection(self, page_id, collection_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def getCollectionListings(self, page_id, collection_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def addListingToCollection(self, page_id, collection_id, listing_id, data: typing.Union[None, dict] = ..., query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def removeListingFromCollection(self, page_id, collection_id, listing_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findPageCollectionsForListings(self, page_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def addCurator(self, page_id, curator_id, data: typing.Union[None, dict] = ..., query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def removeCurator(self, page_id, curator_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def curatorPeopleSearch(self, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findPayment(self, payment_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findPaymentAdjustments(self, payment_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findPaymentAdjustment(self, payment_id, payment_adjustment_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findPaymentAdjustmentItems(self, payment_id, payment_adjustment_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findPaymentAdjustmentItem(self, payment_id, payment_adjustment_id, payment_adjustment_item_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def getPrivateBaseline(self, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def getPropertyOptionModifier(self, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findAllSuggestedPropertyOptions(self, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findPropertySet(self, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def getShop_Receipt2(self, receipt_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def updateReceipt(self, receipt_id, data: typing.Union[None, dict] = ..., query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findAllReceiptListings(self, receipt_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findAllShop_Receipt2Transactions(self, receipt_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findAllRegion(self, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def getRegion(self, region_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findEligibleRegions(self, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def getServerEpoch(self, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def ping(self, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def getShippingCosts(self, shipping_provider_id, data: typing.Union[None, dict] = ..., query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def getShippingInfo(self, shipping_info_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def updateShippingInfo(self, shipping_info_id, data: typing.Union[None, dict] = ..., query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def deleteShippingInfo(self, shipping_info_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def getPostageRates(self, shipping_provider_id, data: typing.Union[None, dict] = ..., query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def createShippingTemplate(self, data: typing.Union[None, dict] = ..., query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def getShippingTemplate(self, shipping_template_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def updateShippingTemplate(self, shipping_template_id, data: typing.Union[None, dict] = ..., query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def deleteShippingTemplate(self, shipping_template_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findAllShippingTemplateEntries(self, shipping_template_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findAllShippingTemplateUpgrades(self, shipping_template_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def createShippingTemplateUpgrade(self, shipping_template_id, data: typing.Union[None, dict] = ..., query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def updateShippingTemplateUpgrade(self, shipping_template_id, data: typing.Union[None, dict] = ..., query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def deleteShippingTemplateUpgrade(self, shipping_template_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def createShippingTemplateEntry(self, data: typing.Union[None, dict] = ..., query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def getShippingTemplateEntry(self, shipping_template_entry_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def updateShippingTemplateEntry(self, shipping_template_entry_id, data: typing.Union[None, dict] = ..., query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def deleteShippingTemplateEntry(self, shipping_template_entry_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findAllShops(self, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def getShop(self, shop_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def updateShop(self, shop_id, data: typing.Union[None, dict] = ..., query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def getShopAbout(self, shop_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def uploadShopBanner(self, shop_id, data: typing.Union[None, dict] = ..., query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def deleteShopBanner(self, shop_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findAllShopCoupons(self, shop_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def createCoupon(self, shop_id, data: typing.Union[None, dict] = ..., query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findCoupon(self, shop_id, coupon_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def updateCoupon(self, shop_id, coupon_id, data: typing.Union[None, dict] = ..., query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def deleteCoupon(self, shop_id, coupon_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findLedger(self, shop_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findLedgerEntries(self, shop_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findLedgerEntry(self, shop_id, ledger_entry_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findPaymentAdjustmentForLedgerEntry(self, shop_id, ledger_entry_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findPaymentForLedgerEntry(self, shop_id, ledger_entry_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findAllShopListingsActive(self, shop_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findAllShopListingsDraft(self, shop_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findAllShopListingsExpired(self, shop_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def getShopListingExpired(self, shop_id, listing_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findAllShopListingsFeatured(self, shop_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findAllShopListingsInactive(self, shop_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def getShopListingInactive(self, shop_id, listing_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findPaymentAccountEntries(self, shop_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findPaymentAdjustmentForPaymentAccountLedgerEntry(self, shop_id, ledger_entry_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findPaymentForPaymentAccountLedgerEntry(self, shop_id, ledger_entry_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findShopPaymentTemplates(self, shop_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def createShopPaymentTemplate(self, shop_id, data: typing.Union[None, dict] = ..., query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def updateShopPaymentTemplate(self, shop_id, payment_template_id, data: typing.Union[None, dict] = ..., query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findAllShopReceipts(self, shop_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findShopPaymentByReceipt(self, shop_id, receipt_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def submitTracking(self, shop_id, receipt_id, data: typing.Union[None, dict] = ..., query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findAllShopReceiptsByStatus(self, shop_id, status, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def searchAllShopReceipts(self, shop_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def getShopReviews(self, shop_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findAllShopSections(self, shop_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def createShopSection(self, shop_id, data: typing.Union[None, dict] = ..., query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def getShopSection(self, shop_id, shop_section_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def updateShopSection(self, shop_id, shop_section_id, data: typing.Union[None, dict] = ..., query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def deleteShopSection(self, shop_id, shop_section_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findAllShopSectionListings(self, shop_id, shop_section_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findAllShopSectionListingsActive(self, shop_id, shop_section_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def getShopSectionTranslation(self, shop_id, shop_section_id, language, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def createShopSectionTranslation(self, shop_id, shop_section_id, language, data: typing.Union[None, dict] = ..., query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def updateShopSectionTranslation(self, shop_id, shop_section_id, language, data: typing.Union[None, dict] = ..., query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def deleteShopSectionTranslation(self, shop_id, shop_section_id, language, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findAllShopTransactions(self, shop_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def getShopTranslation(self, shop_id, language, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def createShopTranslation(self, shop_id, language, data: typing.Union[None, dict] = ..., query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def updateShopTranslation(self, shop_id, language, data: typing.Union[None, dict] = ..., query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def deleteShopTranslation(self, shop_id, language, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def getListingShop(self, listing_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def getBuyerTaxonomy(self, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def getTaxonomyNodeProperties(self, taxonomy_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def getSellerTaxonomy(self, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def getSellerTaxonomyVersion(self, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findSuggestedStyles(self, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findAllTeams(self, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findAllUsersForTeam(self, team_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findTeams(self, team_ids, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def getShop_Transaction(self, transaction_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findAllTreasuries(self, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def getTreasury(self, treasury_key, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def deleteTreasury(self, treasury_key, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findTreasuryComments(self, treasury_key, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def postTreasuryComment(self, treasury_key, data: typing.Union[None, dict] = ..., query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def deleteTreasuryComment(self, treasury_key, comment_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def addTreasuryListing(self, treasury_key, data: typing.Union[None, dict] = ..., query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def removeTreasuryListing(self, treasury_key, listing_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def describeOccasionEnum(self, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def describeRecipientEnum(self, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def describeWhenMadeEnum(self, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def describeWhoMadeEnum(self, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findAllUsers(self, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def getUser(self, user_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findAllUserAddresses(self, user_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def createUserAddress(self, user_id, data: typing.Union[None, dict] = ..., query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def getUserAddress(self, user_id, user_address_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def deleteUserAddress(self, user_id, user_address_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def uploadAvatar(self, user_id, data: typing.Union[None, dict] = ..., query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def getAvatarImgSrc(self, user_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def getUserBillingOverview(self, user_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def getAllUserCarts(self, user_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def addToCart(self, user_id, data: typing.Union[None, dict] = ..., query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def updateCartListingQuantity(self, user_id, data: typing.Union[None, dict] = ..., query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def removeCartListing(self, user_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def getUserCart(self, user_id, cart_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def updateCart(self, user_id, cart_id, data: typing.Union[None, dict] = ..., query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def deleteCart(self, user_id, cart_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def addAndSelectShippingForApplePay(self, user_id, cart_id, data: typing.Union[None, dict] = ..., query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findAllCartListings(self, user_id, cart_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def saveListingForLater(self, user_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def getUserCartForShop(self, user_id, shop_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def createSingleListingCart(self, user_id, data: typing.Union[None, dict] = ..., query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findAllUserCharges(self, user_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def getUserChargesMetadata(self, user_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def getCirclesContainingUser(self, user_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def getConnectedUser(self, user_id, to_user_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def unconnectUsers(self, user_id, to_user_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def listFollowingPages(self, user_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def followPage(self, user_id, data: typing.Union[None, dict] = ..., query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def unfollowPage(self, user_id, page_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def getConnectedUsers(self, user_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def connectUsers(self, user_id, data: typing.Union[None, dict] = ..., query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findAllUserFavoredBy(self, user_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findAllUserFavoriteListings(self, user_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findUserFavoriteListings(self, user_id, listing_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def createUserFavoriteListings(self, user_id, listing_id, data: typing.Union[None, dict] = ..., query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def deleteUserFavoriteListings(self, user_id, listing_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findAllUserFavoriteUsers(self, user_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findUserFavoriteUsers(self, user_id, target_user_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def createUserFavoriteUsers(self, user_id, target_user_id, data: typing.Union[None, dict] = ..., query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def deleteUserFavoriteUsers(self, user_id, target_user_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findAllUserFeedbackAsAuthor(self, user_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findAllUserFeedbackAsBuyer(self, user_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findAllUserFeedbackAsSeller(self, user_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findAllUserFeedbackAsSubject(self, user_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findAllFeedbackFromBuyers(self, user_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findAllFeedbackFromSellers(self, user_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findAllUserPayments(self, user_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findAllUserPaymentTemplates(self, user_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findUserProfile(self, user_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def updateUserProfile(self, user_id, data: typing.Union[None, dict] = ..., query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findAllUserBuyerReceipts(self, user_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findAllUserShippingProfiles(self, user_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findAllUserShops(self, user_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findAllTeamsForUser(self, user_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findAllUserBuyerTransactions(self, user_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...

    def findAllUserTreasuries(self, user_id, query_params: typing.Union[None, dict] = ...) -> rq.EtsyResponse: ...
