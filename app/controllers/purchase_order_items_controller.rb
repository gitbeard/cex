class PurchaseOrderItemsController < ApplicationController
  # GET /purchase_order_items
  # GET /purchase_order_items.json
  def index
    @purchase_order_items = PurchaseOrderItem.all

    respond_to do |format|
      format.html # index.html.erb
      format.json { render json: @purchase_order_items }
    end
  end

  # GET /purchase_order_items/1
  # GET /purchase_order_items/1.json
  def show
    @purchase_order_item = PurchaseOrderItem.find(params[:id])

    respond_to do |format|
      format.html # show.html.erb
      format.json { render json: @purchase_order_item }
    end
  end

  # GET /purchase_order_items/new
  # GET /purchase_order_items/new.json
  def new
    @purchase_order_item = PurchaseOrderItem.new

    respond_to do |format|
      format.html # new.html.erb
      format.json { render json: @purchase_order_item }
    end
  end

  # GET /purchase_order_items/1/edit
  def edit
    @purchase_order_item = PurchaseOrderItem.find(params[:id])
  end

  # POST /purchase_order_items
  # POST /purchase_order_items.json
  def create
    @purchase_order_item = PurchaseOrderItem.new(params[:purchase_order_item])

    respond_to do |format|
      if @purchase_order_item.save
        format.html { redirect_to @purchase_order_item, notice: 'Purchase order item was successfully created.' }
        format.json { render json: @purchase_order_item, status: :created, location: @purchase_order_item }
      else
        format.html { render action: "new" }
        format.json { render json: @purchase_order_item.errors, status: :unprocessable_entity }
      end
    end
  end

  # PUT /purchase_order_items/1
  # PUT /purchase_order_items/1.json
  def update
    @purchase_order_item = PurchaseOrderItem.find(params[:id])

    respond_to do |format|
      if @purchase_order_item.update_attributes(params[:purchase_order_item])
        format.html { redirect_to @purchase_order_item, notice: 'Purchase order item was successfully updated.' }
        format.json { head :no_content }
      else
        format.html { render action: "edit" }
        format.json { render json: @purchase_order_item.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /purchase_order_items/1
  # DELETE /purchase_order_items/1.json
  def destroy
    @purchase_order_item = PurchaseOrderItem.find(params[:id])
    @purchase_order_item.destroy

    respond_to do |format|
      format.html { redirect_to purchase_order_items_url }
      format.json { head :no_content }
    end
  end
end
