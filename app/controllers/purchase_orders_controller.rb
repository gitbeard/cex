class PurchaseOrdersController < ApplicationController
  # GET /purchase_orders
  # GET /purchase_orders.json
  def index
    @purchase_orders = PurchaseOrder.all

    respond_to do |format|
      format.html # index.html.erb
      format.json { render json: @purchase_orders }
    end
  end

  # GET /purchase_orders/1
  # GET /purchase_orders/1.json
  def show
    @purchase_order = PurchaseOrder.find(params[:id])

    respond_to do |format|
      format.html # show.html.erb
      format.json { render json: @purchase_order }
    end
  end

  # GET /purchase_orders/new
  # GET /purchase_orders/new.json
  def new
    @purchase_order = PurchaseOrder.new

    respond_to do |format|
      format.html # new.html.erb
      format.json { render json: @purchase_order }
    end
  end

  # GET /purchase_orders/1/edit
  def edit
    @purchase_order = PurchaseOrder.find(params[:id])
  end

  # POST /purchase_orders
  # POST /purchase_orders.json
  def create
    @purchase_order = PurchaseOrder.new(params[:purchase_order])

    respond_to do |format|
      if @purchase_order.save
        format.html { redirect_to @purchase_order, notice: 'Purchase order was successfully created.' }
        format.json { render json: @purchase_order, status: :created, location: @purchase_order }
      else
        format.html { render action: "new" }
        format.json { render json: @purchase_order.errors, status: :unprocessable_entity }
      end
    end
  end

  # PUT /purchase_orders/1
  # PUT /purchase_orders/1.json
  def update
    @purchase_order = PurchaseOrder.find(params[:id])

    respond_to do |format|
      if @purchase_order.update_attributes(params[:purchase_order])
        format.html { redirect_to @purchase_order, notice: 'Purchase order was successfully updated.' }
        format.json { head :no_content }
      else
        format.html { render action: "edit" }
        format.json { render json: @purchase_order.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /purchase_orders/1
  # DELETE /purchase_orders/1.json
  def destroy
    @purchase_order = PurchaseOrder.find(params[:id])
    @purchase_order.destroy

    respond_to do |format|
      format.html { redirect_to purchase_orders_url }
      format.json { head :no_content }
    end
  end
  
  # Fill in item_numbers by looking up part_numbers
  # Totalize the number of line items, quantities, price save in PO table
  def get_item_numbers
    @purchase_order = PurchaseOrder.find(params[:id])
    @purchase_order.id
    @po_item = PurchaseOrderItem
    @items = Item
    @po_items = @po_item.where("po_id = ? AND item_number = 0", @purchase_order.id)
    
    @po_items.each do |i|
      @some = @items.where("alt_item_number = ?", i.part_number)
      @some.each do |s|
        i.item_number = s.item_number
      end
      i.save
    end
    
    # Totalize section - make a separate task
    @total_lines = 0
    @total_items = 0
    @total_price = 0
    
    @po_items = @po_item.where("po_id = ?", @purchase_order.id)
    @po_items.each do |i|
      @total_lines = @total_lines + 1
      @total_items = @total_items + i.quantity
      @total_price = @total_price + i.extended_price 
    end
    
    @purchase_order.line_items = @total_lines
    @purchase_order.total_items = @total_items
    @purchase_order.total_price = @total_price
    @purchase_order.save
    
    respond_to do |format|
      format.html { redirect_to purchase_orders_url }
      format.json { head :no_content }
    end
  end
  
end
