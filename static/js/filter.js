function onLoadFilter() {
    try {
        const currentUrl = new URL(window.location.href)
        if(currentUrl.searchParams.get('filt_priority')) {
            document.getElementById('filter_priority_min').value = 1
            document.getElementById('filter_priority_max').value = 10
        } else {
            var filterParameterfromUrl = currentUrl.searchParams.get('filt_priority')
            var filtParamList = filterParameterfromUrl.split(',')
            var filter_by_prioritypoint_min = Number(filtParamList[0])
            var filter_by_prioritypoint_max = Number(filtParamList[1])
            document.getElementById('filter_priority_min').value = filter_by_prioritypoint_min
            document.getElementById('filter_priority_max').value = filter_by_prioritypoint_max
        }
    } catch (error) {
        console.log(
            error
        )
    }
}
onLoadFilter()


function filter_form() {
    const currentUrl = new URL(window.location.href)

    var filter_by_status = document.getElementsByName('filt_stat')
    var filter_by_category = document.getElementsByName('filt_categ')
    var filter_by_categList = []
    var filter_by_prioritypoint_min = parseInt(document.getElementById('filter_priority_min').value)
    var filter_by_prioritypoint_max = parseInt(document.getElementById('filter_priority_max').value)
    var filter_by_ppList = [filter_by_prioritypoint_min,filter_by_prioritypoint_max]
    var filter_by_type = document.getElementsByName('filt_type')

    for(i=0; i<filter_by_status.length; i++) {
        if(filter_by_status[i].checked) {
            var filt_stat = filter_by_status[i].value
        }
    }
    for(i=0; i<filter_by_category.length; i++) {
        if(filter_by_category[i].checked == true) {
            filter_by_categList.push(filter_by_category[i].value)
        }
    }
    for(i=0; i<filter_by_type.length; i++) {
        if(filter_by_type[i].checked) {
            var filt_type = filter_by_type[i].value
        }
    }

    // console.log(filt_stat, '|', filter_by_categList, '|', filter_by_ppList, '|', filt_type)

    currentUrl.searchParams.set('filt_stat', filt_stat)
    currentUrl.searchParams.set('filt_categ', filter_by_categList)
    currentUrl.searchParams.set('filt_priority', filter_by_ppList)
    currentUrl.searchParams.set('filt_type', filt_type)

    window.history.pushState({}, '', currentUrl)
    // window.reload() // WINDOW RELOAD ERROR ?
    // window.location.reload()
    location.reload()
}



// ===================== ASCII URL PARAMETERS WITH % HEX ===================== //
// +----+-----+----+-----+----+-----+----+-----+
// | Hx | Chr | Hx | Chr | Hx | Chr | Hx | Chr |
// +----+-----+----+-----+----+-----+----+-----+
// | 00 | NUL | 20 | SPC | 40 |  @  | 60 |  `  |
// | 01 | SOH | 21 |  !  | 41 |  A  | 61 |  a  |
// | 02 | STX | 22 |  "  | 42 |  B  | 62 |  b  |
// | 03 | ETX | 23 |  #  | 43 |  C  | 63 |  c  |
// | 04 | EOT | 24 |  $  | 44 |  D  | 64 |  d  |
// | 05 | ENQ | 25 |  %  | 45 |  E  | 65 |  e  |
// | 06 | ACK | 26 |  &  | 46 |  F  | 66 |  f  |
// | 07 | BEL | 27 |  '  | 47 |  G  | 67 |  g  |
// | 08 | BS  | 28 |  (  | 48 |  H  | 68 |  h  |
// | 09 | TAB | 29 |  )  | 49 |  I  | 69 |  i  |
// | 0A | LF  | 2A |  *  | 4A |  J  | 6A |  j  |
// | 0B | VT  | 2B |  +  | 4B |  K  | 6B |  k  |
// | 0C | FF  | 2C |  ,  | 4C |  L  | 6C |  l  |
// | 0D | CR  | 2D |  -  | 4D |  M  | 6D |  m  |
// | 0E | SO  | 2E |  .  | 4E |  N  | 6E |  n  |
// | 0F | SI  | 2F |  /  | 4F |  O  | 6F |  o  |
// | 10 | DLE | 30 |  0  | 50 |  P  | 70 |  p  |
// | 11 | DC1 | 31 |  1  | 51 |  Q  | 71 |  q  |
// | 12 | DC2 | 32 |  2  | 52 |  R  | 72 |  r  |
// | 13 | DC3 | 33 |  3  | 53 |  S  | 73 |  s  |
// | 14 | DC4 | 34 |  4  | 54 |  T  | 74 |  t  |
// | 15 | NAK | 35 |  5  | 55 |  U  | 75 |  u  |
// | 16 | SYN | 36 |  6  | 56 |  V  | 76 |  v  |
// | 17 | ETB | 37 |  7  | 57 |  W  | 77 |  w  |
// | 18 | CAN | 38 |  8  | 58 |  X  | 78 |  x  |
// | 19 | EM  | 39 |  9  | 59 |  Y  | 79 |  y  |
// | 1A | SUB | 3A |  :  | 5A |  Z  | 7A |  z  |
// | 1B | ESC | 3B |  ;  | 5B |  [  | 7B |  {  |
// | 1C | FS  | 3C |  <  | 5C |  \  | 7C |  |  |
// | 1D | GS  | 3D |  =  | 5D |  ]  | 7D |  }  |
// | 1E | RS  | 3E |  >  | 5E |  ^  | 7E |  ~  |
// | 1F | US  | 3F |  ?  | 5F |  _  | 7F | DEL |
// +----+-----+----+-----+----+-----+----+-----+
