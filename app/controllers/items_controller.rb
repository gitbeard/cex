class ItemsController < ApplicationController
  # GET /items
  # GET /items.json
  def index
    @items = Item.all

    respond_to do |format|
      format.html # index.html.erb
      format.json { render json: @items }
    end
  end

  # GET /items/1
  # GET /items/1.json
  def show
    @item = Item.find(params[:id])
    @daily_inventories = DailyInventory
    @purchase_order_items = PurchaseOrderItem
    inv_data = Array.new
    @inventory = @daily_inventories.where("item_number = ?", @item.item_number)
    @inventory.each do |inv|
      inv_data.push(inv.quantity)
    end
    
    
    
    @h = LazyHighCharts::HighChart.new('graph') do |f|
      f.options[:chart][:height] = 900
      f.series(:name=>'John', :data=>inv_data) #[3, 20, 3, 5, 4, 10, 12 ,3, 5,6,7,7,80,9,9])
      #f.series(:name=>'Jane', :data=> [1, 3, 4, 3, 3, 5, 4,-46,7,8,8,9,9,0,0,9] )
    end 

    respond_to do |format|
      format.html # show.html.erb
      format.json { render json: @item }
    end
  end
  
  # GET /xl_rep
  # GET /xl_rep.json
  def xl_rep
    @items = Item
    @daily_inventories = DailyInventory
    @parts = Part
    
    respond_to do |format|
      format.html # show.html.erb
      format.json { render json: @item }
    end
  end


  # GET /items/1
  # GET /items/1.json
  # Show all the data for this part_number (all lengths)
  def show_all_lengths
    @item = Item.find(params[:id])
    @item_all = Item
    @items = @item_all.where("part_number = ?", @item.part_number)
    
    
    @daily_inventories = DailyInventory
    
    
    @h = LazyHighCharts::HighChart.new('graph') do |f|
      f.options[:chart][:height] = 900
      f.options[:chart][:type] = "line"
      f.options[:chart][:zoomType] = "x"
      #f.options[:plotOptions][:line][:marker][:enabled] = false
      last_inv = 0
      @items.each do |i|
        inv_data = Array.new
        @inventory = @daily_inventories.where("item_number = ?", i.item_number)
        @inventory.each do |inv|
          change = inv.quantity #- last_inv
          last_inv = inv.quantity
          inv_data.push([inv.datetime,change])
          #f.options[:tooltip][:valueSuffix] = inv.quantity.to_s
        end
        
        f.series(:name=>i.part_length, :data=>inv_data)
      end
      #f.series(:name=>'John', :data=>inv_data) #[3, 20, 3, 5, 4, 10, 12 ,3, 5,6,7,7,80,9,9])
      #f.series(:name=>'Jane', :data=> [1, 3, 4, 3, 3, 5, 4,-46,7,8,8,9,9,0,0,9] )
    end 

    respond_to do |format|
      format.html # show.html.erb
      format.json { render json: @item }
    end
  end

  def show_all_lengths_change
    @item = Item.find(params[:id])
    @item_all = Item
    @items = @item_all.where("part_number = ?", @item.part_number)
    
    
    @daily_inventories = DailyInventory
    
    
    @h = LazyHighCharts::HighChart.new('graph') do |f|
      f.options[:chart][:height] = 900
      f.options[:chart][:type] = "line"
      f.options[:chart][:zoomType] = "x"
      #f.options[:plotOptions][:line][:marker][:enabled] = false
      last_inv = 0
      @items.each do |i|
        inv_data = Array.new
        @inventory = @daily_inventories.where("item_number = ?", i.item_number)
        @inventory.each do |inv|
          change = inv.quantity - last_inv
          last_inv = inv.quantity
          inv_data.push([inv.datetime,change])
          #f.options[:tooltip][:valueSuffix] = inv.quantity.to_s
        end
        
        f.series(:name=>i.part_length, :data=>inv_data)
      end
      #f.series(:name=>'John', :data=>inv_data) #[3, 20, 3, 5, 4, 10, 12 ,3, 5,6,7,7,80,9,9])
      #f.series(:name=>'Jane', :data=> [1, 3, 4, 3, 3, 5, 4,-46,7,8,8,9,9,0,0,9] )
    end 

    respond_to do |format|
      format.html # show.html.erb
      format.json { render json: @item }
    end
  end



  # GET /items/new
  # GET /items/new.json
  def new
    @item = Item.new

    respond_to do |format|
      format.html # new.html.erb
      format.json { render json: @item }
    end
  end

  # GET /items/1/edit
  def edit
    @item = Item.find(params[:id])
  end

  # POST /items
  # POST /items.json
  def create
    @item = Item.new(params[:item])

    respond_to do |format|
      if @item.save
        format.html { redirect_to @item, notice: 'Item was successfully created.' }
        format.json { render json: @item, status: :created, location: @item }
      else
        format.html { render action: "new" }
        format.json { render json: @item.errors, status: :unprocessable_entity }
      end
    end
  end

  # PUT /items/1
  # PUT /items/1.json
  def update
    @item = Item.find(params[:id])

    respond_to do |format|
      if @item.update_attributes(params[:item])
        format.html { redirect_to @item, notice: 'Item was successfully updated.' }
        format.json { head :no_content }
      else
        format.html { render action: "edit" }
        format.json { render json: @item.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /items/1
  # DELETE /items/1.json
  def destroy
    @item = Item.find(params[:id])
    @item.destroy

    respond_to do |format|
      format.html { redirect_to items_url }
      format.json { head :no_content }
    end
  end
end
